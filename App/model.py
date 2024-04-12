"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.Algorithms.Sorting import customsort as cus
from datetime import datetime as date
assert cf



# Construccion de modelos
sort_algorithm = cus #SE SELECCIONA TIMSORT COMO ALGORITMO POR DEFECTO
# construccion de modelos

def new_catalog():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {'Trabajos': None,
               'mapa_ids': None,
               'mapa_paises': None,
               'mapa_fechas': None,
               'mapa_ciudades': None,
               'habilidades_id': None,
               'habilidades_name': None,
               'employment_types_id': None,
               'multilocations_id': None,}
    
    # Lista con todos los trabajos encontrados en el archivo de carga
    catalog['Trabajos'] = lt.newList('ARRAY_LIST', compareJobIds)
    # Indices por diferentes criterios para llegar a la info consultada, no replican la info, referencian los libros de la lista
    # Estructura para guardar los datos correspondientes a los ID's
    catalog["mapa_ids"] = mp.newMap(60000,
                                    maptype="CHAINING",
                                    loadfactor=8)
    # Estructura para guardar datos según el país
    catalog["mapa_paises"] = mp.newMap(390,
                                       maptype="CHAINING",
                                       loadfactor=4)
    # Estructura para guardar datos segun la ciudad
    catalog["mapa_ciudades"] = mp.newMap(10000,
                                         maptype="CHAINING",
                                         loadfactor=4)
    # Estrcutura para guardar datos segun empresa
    catalog["mapa_empresas"] = mp.newMap(10000,
                                         maptype="CHAINING",
                                         loadfactor=4)
    # Estrcutura para guardar datos segun experiencia
    catalog["mapa_experiencia"] = mp.newMap(10000,
                                         maptype="CHAINING",
                                         loadfactor=4)

    #catalog["mapa_fechas"] = mp.newMap(60000,maptype="CHAINING") # No seguro si usar este

    # EStructuras de datos para guardar info del csv skills
    catalog["habilidades_id"] = mp.newMap(10000,
                                          maptype="CHAINING",
                                          loadfactor = 4) 
    catalog["habilidades_name"] = mp.newMap(10000,maptype="CHAINING",
                                            loadfactor = 4) 
    # EStructuras de datos para guardar info del csv emlpoyment types
    catalog['employment_types_id'] = mp.newMap(10000,
                                               maptype = "CHAINING",
                                               loadfactor = 4)
    # EStructuras de datos para guardar info del csv multilocation
    catalog['multilocations_id'] = mp.newMap(10000,
                                               maptype = "CHAINING",
                                               loadfactor = 4)
    return catalog


# Funciones para agregar informacion al modelo

def add_data_jobs(catalog, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos
    #IDs
    lt.addLast(catalog['Trabajos'], job)
    mp.put(catalog['mapa_ids'],job['id'], job)
    add_job_country(catalog, job['country_code'], job)
    add_job_city(catalog, job['city'], job)
    add_job_company(catalog, job['company_name'], job) # empresas
    add_job_experience(catalog, job['experience_level'], job)    # experiencia
    
def add_job_country(catalog, country_code, job):
    countries = catalog['mapa_paises']
    existcountry = mp.contains(countries, country_code)
    if existcountry:
        entry = mp.get(countries, country_code)
        country = me.getValue(entry)
    else:
        country = new_country(country_code)
        mp.put(countries, country_code, country)
    lt.addLast(country['jobs'], job)
    country['size'] = lt.size(country['jobs'])
    
def add_job_city(catalog, city, job):
    cities = catalog['mapa_ciudades']
    existcity = mp.contains(cities, city)
    if existcity:
        entry = mp.get(cities, city)
        citytemp = me.getValue(entry)
    else:
        citytemp = new_city(city)
        mp.put(cities, city, citytemp)
    lt.addLast(citytemp['jobs'], job)  
    citytemp['size'] = lt.size(citytemp['jobs'])
    
def add_job_company(catalog, company, job):
    companies = catalog['mapa_empresas']
    existcompany = mp.contains(companies, company)
    if existcompany:
        entry = mp.get(companies, company)
        companytemp = me.getValue(entry)
    else:
        companytemp = new_company(company)
        mp.put(companies, company, companytemp)
    lt.addLast(companytemp['jobs'], job)  
    companytemp['size'] = lt.size(companytemp['jobs'])

def add_job_experience(catalog, experience, job):
    experiences = catalog['mapa_experiencia']
    exist = mp.contains(experiences, experience)
    if exist:
        entry = mp.get(experiences, experience)
        experiencetemp = me.getValue(entry)
    else:
        experiencetemp = new_experience(experience)
        mp.put(experiences, experience, experiencetemp)
    lt.addLast(experiencetemp['jobs'], job)  
    experiencetemp['size'] = lt.size(experiencetemp['jobs'])
      

def new_country(country_code):
    country = {'country_code': "",
               "jobs": None,
               "size": 0}
    country['country_code'] = country_code
    country['jobs'] = lt.newList('ARRAY_LIST', compareCountry)
    return country
        
 
def new_city(city_in):
    city = {'city': "",
               "jobs": None,
               "size": 0}
    city['city'] = city_in
    city['jobs'] = lt.newList('ARRAY_LIST', compareCity)  
    return city 

def new_company(company_in):
    company = {'company': "",
               "jobs": None,
               "size": 0}
    company['city'] = company_in
    company['jobs'] = lt.newList('ARRAY_LIST')
    return company 

def new_experience(experience_in):
    experience = {'company': "",
               "jobs": None,
               "size": 0}
    experience['city'] = experience_in
    experience['jobs'] = lt.newList('ARRAY_LIST')
    return experience            
    
def add_data_skills(catalog, row):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Crear mapa de habilidades segun el id
    skills_id = catalog['habilidades_id']
    idr = row['id']
        
    existid = mp.contains(skills_id, idr)
    if existid:
        entry = mp.get(skills_id, idr)
        id = me.getValue(entry)
    else:
        id = new_skills_id(idr)
        mp.put(skills_id, idr, id)
    lt.addLast(id['row'], row)

    
    #Crear mapa de habilidades segun nombre de la habilidad
    try:
        skills_name = catalog['habilidades_name']
        namer = row['name']
        
        existname = mp.contains(skills_name, namer)
        if existname:
            entry = mp.get(skills_name, namer)
            name = me.getValue(entry)
        else:
            name = new_skills_name(namer)
            mp.put(skills_name, namer, name)
        lt.addLast(name['row'], row)
    except Exception:
        return None
    
def new_skills_id(idr):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'id': "", "row": None}
    entry['id'] = idr
    entry['row'] = lt.newList('ARRAY_LIST')
    return entry

def new_skills_name(namer):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'id': "", "row": None}
    entry['name'] = namer
    entry['row'] = lt.newList('ARRAYLIST')
    return entry

def add_data_employment_types(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass
def add_data_multilocation(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass



# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def jobs_id_size(catalog):
    """
    Numero de id de ofertas en el catalogo
    """
    return mp.size(catalog['mapa_ids'])

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def sort_country_experience(catalog, pais, experiencia): # REQUERIMIENTO 1 --------------------------------------------------------------------------
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    jobsf = lt.newList("ARRAY_LIST")
    
    jobs_p = me.getValue(mp.get(catalog['mapa_paises'], pais))["jobs"]    # pais
    jobs_e = me.getValue(mp.get(catalog['mapa_experiencia'], experiencia))["jobs"]    # experiencia
  
    if (lt.size(jobs_p) <= lt.size(jobs_e)): # Revisar camino con menor cantidad de comparaciones
        for job in lt.iterator(jobs_e):
            if (flt_experiencia(job, experiencia) == True): # REALIZAR FUNCIONES DE FILTRADO Y VERIFICAR OUTPUT
                lt.addLast(jobsf,job)
    else: 
        for job in lt.iterator(jobs_e):
            if (flt_pais(job, pais) == True):
                lt.addLast(jobsf, job)
    
    jobsfsize = lt.size(jobsf) 
    if jobsfsize != 0:
        jobsf = sort_algorithm.sort(jobsf, cmp_fecha_empresa)
        catalog['REQ1'] = jobsf   
        
    return catalog, jobsfsize   

def sort_company_city(catalog, empresa, ciudad): # REQUERIMIENTO 2 ----------------------------------------------------
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    jobsf = lt.newList("ARRAY_LIST")

    jobs_c = me.getValue(mp.get(catalog['mapa_ciudades'], ciudad))["jobs"]    # Ciudad
    jobs_e = me.getValue(mp.get(catalog['mapa_empresas'], empresa))["jobs"]  # Empresa
    
    if (lt.size(jobs_c) <= lt.size(jobs_e)): # Revisar camino con menor cantidad de comparaciones
        for job in lt.iterator(jobs_c):
            if (flt_empresa(job, empresa) == True):
                lt.addLast(jobsf,job)
    else: 
        for job in lt.iterator(jobs_e):
            if (flt_ciudad(job, ciudad) == True):
                lt.addLast(jobsf, job)
    
    jobsfsize = lt.size(jobsf) 
    if jobsfsize != 0:
        jobsf = sort_algorithm.sort(jobsf, cmp_fecha_empresa)
        catalog['REQ2'] = jobsf   
        
    return catalog, jobsfsize 


# Función para filtrar las ofertas de trabajo por empresa y fecha
def filter_jobs_by_company_and_date(catalog, company_name, start_date, end_date):  # REQUERIMIENTO 3 ----------------------------------------------------
    """
    Filtra las ofertas de trabajo por empresa y fecha
    """
    # Lista para almacenar las ofertas que cumplen con los criterios de filtrado
    filtered_jobs = []
    
    # Iterar sobre todas las ofertas en el catálogo
    for job in catalog:
        # Verificar si la oferta pertenece a la empresa especificada
        # y si su fecha de publicación está dentro del rango especificado
        if job['company_name'] == company_name and start_date <= job['published_at'] <= end_date:
            filtered_jobs.append(job)
    
    return filtered_jobs



def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def sort_city_date(catalog, ciudad, fecha1, fecha2): # REQUERIMIENTO 5 -------------------------------------------------
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5

    jobs = mp.get(catalog['mapa_ciudades'], ciudad)
    jobsf = lt.newList('ARRAY_LIST')
    
    empresas = {} #Diccionario con nombre de empresa y # de ofertas
    ofertasmax = 0
    empresamax = None
    empresamin = None
    
    if jobs:
        #recuperar lista de ofertas
        jobs_city = me.getValue(jobs)['jobs']
        for job in lt.iterator(jobs_city):
            if (flt_rango_fechas(job, fecha1, fecha2) == True): # Filtrar ofertas entre las fechas deseadas
                lt.addLast(jobsf, job)
                 
                if job['company_name'] in empresas: #Contador de ofertas por empresa para saber maximo y minimo
                    empresas[job['company_name']] += 1 
                    if ofertasmax < empresas[job['company_name']]: #Identificar maximo 
                        ofertasmax = empresas[job['company_name']]
                        empresamax = job['company_name']                    
                else:
                    empresas[job['company_name']] = 1 
                      
        for empresa in empresas: # INCLUIR DENTRO DE 1 CICLO FOR NO 2
            if empresas[empresa] <= ofertasmax:
                ofertasmin = empresas[empresa]
                empresamin = empresa   
                
        max = (empresamax, ofertasmax)
        
        if lt.size(jobsf) == 1:
            min = max
        else:
            min = (empresamin, ofertasmin)
        
        jobsfsize = lt.size(jobsf)
        if jobsfsize != 0:
            jobsf = sort_algorithm.sort(jobsf, cmp_fecha_empresa)
            catalog['REQ5'] = jobsf     
        
        return catalog, jobsfsize, max, min 

def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs): # REQUERIMIENTO 7 -----------------------------------------------------------------------------------------
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


def selectDataSize(algo_opt):
    """
    Función para escoger el tipo de archivo con el que se ejecuta el programa
    """
    #Rta por defecto
    DataSize = 10
    Sizemsg = "Se escogió por defecto la opción 10 - small"
    
    if algo_opt == 1:
        DataSize = "10-por-"
        Sizemsg = "Se ha escogido el tamaño 10-por"
        
    elif algo_opt == 2:
        DataSize = "20-por-"
        Sizemsg = "Se ha escogido el tamaño 20-por"

    elif algo_opt == 3:
        DataSize = "30-por-"
        Sizemsg = "Se ha escogido el tamaño 30-por"

    elif algo_opt == 4:
        DataSize = "40-por-"
        Sizemsg = "Se ha escogido el tamaño 40-por"
        
    elif algo_opt == 5:
        DataSize = "50-por-"
        Sizemsg = "Se ha escogido el tamaño 50-por"
        
    elif algo_opt == 6:
        DataSize = "60-por-"
        Sizemsg = "Se ha escogido el tamaño 60-por"
        
    elif algo_opt == 7:
        DataSize = "70-por-"
        Sizemsg = "Se ha escogido el tamaño 70-por"
        
    elif algo_opt == 8:
        DataSize = "80-por-"
        Sizemsg = "Se ha escogido el tamaño 80-por"
        
    elif algo_opt == 9:
        DataSize = "90-por-"
        Sizemsg = "Se ha escogido el tamaño 90-por"
        
    elif algo_opt == 10:
        DataSize = "small-"
        Sizemsg = "Se ha escogido el tamaño small-"
        
    elif algo_opt == 11:
        DataSize = "medium-"
        Sizemsg = "Se ha escogido el tamaño medium-"
        
    elif algo_opt == 12:
        DataSize = "large-"
        Sizemsg = "Se ha escogido el tamaño large-"
    return DataSize, Sizemsg

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass



def compareJobIds(id1, id2):
    """
    Compara dos ids de dos trabajos
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
    

def compareMapJobIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareCountry(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareCity(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
    
def flt_rango_fechas(oferta, fecha1, fecha2): # Filtrado por fechas - REQ 5
    if ((date.strptime(oferta["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") >= date.strptime(fecha1,"%Y-%m-%d")) and 
        (date.strptime(oferta["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") <= date.strptime(fecha2,"%Y-%m-%d"))):
        return True
    else: return False
    
def flt_experiencia(oferta, experiencia): # Filtrado REQ 1
    if (oferta["experience_level"] == experiencia): return True
    else: return False
    
def flt_pais(oferta, pais): # Filtrado REQ 1
    if (oferta["country_code"] == pais): return True
    else: return False

def flt_empresa(oferta, empresa): # Filtrado por empresa - REQ 2
    if oferta['company_name'] == empresa:
        return True
    else: return False

def flt_ciudad(oferta, ciudad): # Filtrado por ciudad - REQ 2
    if oferta['city'] == ciudad:
        return True
    else: return False

    
def cmp_fecha_empresa(oferta1, oferta2): #Criterio ordenamiento RQ 5 - Fecha mayor a menor, si igual, nombre de empresa de A-Z
    if (date.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") > date.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")):
        return True
    elif (date.strptime(oferta1["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ") == date.strptime(oferta2["published_at"],"%Y-%m-%dT%H:%M:%S.%fZ")):
        if (oferta1["company_name"] <= oferta2["company_name"]):
            return True
        else: return False
    else: return False
    
# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(list, cmp):
    """
    Función encargada de ordenar la lista con los datos
    """
    return sort_algorithm.sort(list, cmp)
    
