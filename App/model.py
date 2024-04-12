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
#from DISClib.Algorithms.Sorting import customsort as cus
from datetime import datetime as date
assert cf



# Construccion de modelos
#sort_algorithm = cus #SE SELECCIONA TIMSORT COMO ALGORITMO POR DEFECTO
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
        jobsf = sa.sort(jobsf, cmp_fecha_empresa)
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
        jobsf = sa.sort(jobsf, cmp_fecha_empresa)
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



from DISClib.Utils import TADList, TADMap

def req4(catalog, codigo_pais, fecha1, fecha2):
    """
    Función que filtra las ofertas de trabajo por país y rango de fechas,
    cuenta el número total de ofertas, empresas y ciudades, y identifica
    la ciudad con mayor y menor número de ofertas.
    """
    # Crear un mapa para contar ofertas por ciudad
    contador_ciudades = TADMap.newMap(maptype='CHAINING')
    # Crear un mapa para contar ofertas por empresa
    empresas = TADMap.newMap(maptype='CHAINING')
    ofertasmax = 0
    empresamax = None
    empresamin = None
    ofertasmin = 0
    
    # Iterar sobre todas las ciudades en el país
    for ciudad in mp.keySet(catalog['mapa_ciudades']):
        if mp.get(catalog['mapa_ciudades'], ciudad)['pais'] == codigo_pais:
            jobs_city = lt.newList(datastructure='SINGLE_LINKED')
            for job in lt.iterator(jobs_city):
                if flt_rango_fechas(job, fecha1, fecha2): # Filtrar ofertas entre las fechas deseadas
                    # Actualizar contador_ciudades
                    if mp.contains(contador_ciudades, ciudad):
                        mp.put(contador_ciudades, ciudad, mp.get(contador_ciudades, ciudad) + 1)
                    else:
                        mp.put(contador_ciudades, ciudad, 1)
                    
                    # Actualizar empresas
                    if mp.contains(empresas, job['company_name']):
                        mp.put(empresas, job['company_name'], mp.get(empresas, job['company_name']) + 1)
                        if ofertasmax < mp.get(empresas, job['company_name']):
                            ofertasmax = mp.get(empresas, job['company_name'])
                            empresamax = job['company_name']
                    else:
                        mp.put(empresas, job['company_name'], 1)
    
    # Identificar la ciudad con mayor y menor número de ofertas
    ciudad_mayor_ofertas = max(mp.keySet(contador_ciudades), key=lambda x: mp.get(contador_ciudades, x))
    ciudad_menor_ofertas = min(mp.keySet(contador_ciudades), key=lambda x: mp.get(contador_ciudades, x))
    
    # Preparar la respuesta
    respuesta = {
        "total_ofertas": sum(mp.valueSet(contador_ciudades)),
        "total_empresas": mp.size(empresas),
        "total_ciudades": mp.size(contador_ciudades),
        "ciudad_mayor_ofertas": {ciudad_mayor_ofertas: mp.get(contador_ciudades, ciudad_mayor_ofertas)},
        "ciudad_menor_ofertas": {ciudad_menor_ofertas: mp.get(contador_ciudades, ciudad_menor_ofertas)},
        "empresa_max_ofertas": {empresamax: ofertasmax},
        "empresa_min_ofertas": {empresamin: ofertasmin}
    }
    
    return respuesta


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
            jobsf = sa.sort(jobsf, cmp_fecha_empresa)
            catalog['REQ5'] = jobsf     
        
        return catalog, jobsfsize, max, min 

def req_6(ofertas, N, nivel_experticia, año):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    # Filtrar ofertas por año y nivel de experiencia
    ofertas_filtradas = [oferta for oferta in ofertas if oferta['año'] == año and (nivel_experticia == 'indiferente' or oferta['experiencia'] == nivel_experticia)]
    
    # Diccionario para contar ofertas por ciudad
    contador_ciudades = {}
    # Diccionario para contar empresas por ciudad
    empresas_ciudad = {}
    # Diccionario para almacenar la información de las ciudades
    info_ciudades = {}
    
    for oferta in ofertas_filtradas:
        ciudad = oferta['ciudad']
        if ciudad not in contador_ciudades:
            contador_ciudades[ciudad] = 1
            empresas_ciudad[ciudad] = {oferta['nombre_empresa']: 1}
            info_ciudades[ciudad] = {'total_ofertas': 1, 'empresas': 1, 'salario_promedio': oferta['salario'], 'mejor_oferta': oferta, 'peor_oferta': oferta}
        else:
            contador_ciudades[ciudad] += 1
            if oferta['nombre_empresa'] not in empresas_ciudad[ciudad]:
                empresas_ciudad[ciudad][oferta['nombre_empresa']] = 1
            else:
                empresas_ciudad[ciudad][oferta['nombre_empresa']] += 1
            info_ciudades[ciudad]['total_ofertas'] += 1
            info_ciudades[ciudad]['empresas'] = len(empresas_ciudad[ciudad])
            info_ciudades[ciudad]['salario_promedio'] = (info_ciudades[ciudad]['salario_promedio'] + oferta['salario']) / 2
            if oferta['salario'] > info_ciudades[ciudad]['mejor_oferta']['salario']:
                info_ciudades[ciudad]['mejor_oferta'] = oferta
            if oferta['salario'] < info_ciudades[ciudad]['peor_oferta']['salario']:
                info_ciudades[ciudad]['peor_oferta'] = oferta
    
    # Ordenar ciudades por número de ofertas
    ciudades_ordenadas = sorted(info_ciudades.items(), key=lambda x: x[1]['total_ofertas'], reverse=True)
    
    # Preparar la respuesta
    respuesta = {
        "total_ciudades": len(ciudades_ordenadas),
        "total_empresas": sum(info_ciudades[ciudad]['empresas'] for ciudad in info_ciudades),
        "total_ofertas": sum(info_ciudades[ciudad]['total_ofertas'] for ciudad in info_ciudades),
        "ciudad_mayor_ofertas": ciudades_ordenadas[0][0],
        "ciudad_menor_ofertas": ciudades_ordenadas[-1][0],
        "ciudades": []
    }
    
    for ciudad, info in ciudades_ordenadas:
        if len(respuesta['ciudades']) < N:
            respuesta['ciudades'].append({
                "nombre_ciudad": ciudad,
                "pais": info['pais'],
                "total_ofertas": info['total_ofertas'],
                "salario_promedio": info['salario_promedio'],
                "empresas": info['empresas'],
                "empresa_max_ofertas": max(empresas_ciudad[ciudad   ].items(), key=lambda x: x[1])[0],
                "mejor_oferta": info['mejor_oferta'],
                "peor_oferta": info['peor_oferta']
            })
    
    return respuesta


def req_7(ofertas, N, año, mes): # REQUERIMIENTO 7 -----------------------------------------------------------------------------------------
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    # Filtrar ofertas por año y mes
    ofertas_filtradas = [oferta for oferta in ofertas if oferta['año'] == año and oferta['mes'] == mes]
    
    # Diccionario para contar ofertas por país y ciudad
    contador_paises = {}
    contador_ciudades = {}
    # Diccionario para almacenar la información de las habilidades por nivel de experiencia
    info_habilidades = {'junior': {}, 'mid': {}, 'senior': {}}
    
    for oferta in ofertas_filtradas:
        pais = oferta['pais']
        ciudad = oferta['ciudad']
        experiencia = oferta['experiencia']
        
        if pais not in contador_paises:
            contador_paises[pais] = 1
            contador_ciudades[ciudad] = 1
        else:
            contador_paises[pais] += 1
            contador_ciudades[ciudad] += 1
        
        # Contar habilidades por nivel de experiencia
        for habilidad in oferta['habilidades']:
            if habilidad not in info_habilidades[experiencia]:
                info_habilidades[experiencia][habilidad] = 1
            else:
                info_habilidades[experiencia][habilidad] += 1
    
    # Ordenar países y ciudades por número de ofertas
    paises_ordenados = sorted(contador_paises.items(), key=lambda x: x[1], reverse=True)
    ciudades_ordenadas = sorted(contador_ciudades.items(), key=lambda x: x[1], reverse=True)
    
    # Preparar la respuesta
    respuesta = {
        "total_ofertas": len(ofertas_filtradas),
        "total_ciudades": len(contador_ciudades),
        "pais_mayor_ofertas": paises_ordenados[0][0],
        "ciudad_mayor_ofertas": ciudades_ordenadas[0][0],
        "info_habilidades": {}
    }
    
    for nivel in info_habilidades:
        habilidades_ordenadas = sorted(info_habilidades[nivel].items(), key=lambda x: x[1], reverse=True)
        respuesta['info_habilidades'][nivel] = {
            "total_habilidades": len(habilidades_ordenadas),
            "habilidad_mas_solicitada": habilidades_ordenadas[0][0],
            "habilidad_menos_solicitada": habilidades_ordenadas[-1][0],
            "nivel_promedio": sum(info_habilidades[nivel].values()) / len(info_habilidades[nivel]),
            "empresas": {},
            "empresa_max_ofertas": {},
            "empresa_min_ofertas": {}
        }
    
    # Aquí se debe completar la lógica para calcular el conteo de empresas, la empresa con mayor número de ofertas, y la empresa con menor número de ofertas para cada nivel de experiencia.
    # Esto requiere un análisis adicional de las ofertas filtradas por nivel de experiencia y país/ciudad.
    
    return respuesta


def req_8(  ofertas, nivel_experticia, divisa, fecha_inicial, fecha_final):

    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    # Filtrar ofertas por nivel de experticia, divisa y rango de fechas
    ofertas_filtradas = [oferta for oferta in ofertas if (nivel_experticia == 'indiferente' or oferta['experiencia'] == nivel_experticia) and oferta['divisa'] == divisa and fecha_inicial <= oferta['fecha'] <= fecha_final]
    
    # Diccionario para contar ofertas por país y ciudad
    contador_paises = {}
    contador_ciudades = {}
    # Diccionario para almacenar la información de las ofertas por país
    info_paises = {}
    
    for oferta in ofertas_filtradas:
        pais = oferta['pais']
        ciudad = oferta['ciudad']
        
        if pais not in contador_paises:
            contador_paises[pais] = 1
            contador_ciudades[ciudad] = 1
            info_paises[pais] = {'total_ofertas': 1, 'empresas': {oferta['nombre_empresa']: 1}, 'salario_promedio': oferta['salario'], 'habilidades': oferta['habilidades']}
        else:
            contador_paises[pais] += 1
            contador_ciudades[ciudad] += 1
            info_paises[pais]['total_ofertas'] += 1
            if oferta['nombre_empresa'] not in info_paises[pais]['empresas']:
                info_paises[pais]['empresas'][oferta['nombre_empresa']] = 1
            else:
                info_paises[pais]['empresas'][oferta['nombre_empresa']] += 1
            info_paises[pais]['salario_promedio'] = (info_paises[pais]['salario_promedio'] + oferta['salario']) / 2
            info_paises[pais]['habilidades'].extend(oferta['habilidades'])
    
    # Ordenar países por promedio de oferta salarial
    paises_ordenados = sorted(info_paises.items(), key=lambda x: x[1]['salario_promedio'], reverse=True)
    
    # Preparar la respuesta
    respuesta = {
        "total_empresas": len(set(empresa for pais in info_paises.values() for empresa in pais['empresas'].keys())),
        "total_ofertas": sum(info_paises[pais]['total_ofertas'] for pais in info_paises),
        "total_paises": len(contador_paises),
        "total_ciudades": len(contador_ciudades),
        "paises": []
    }
    
    for pais, info in paises_ordenados:
        if len(respuesta['paises']) < 10:
            respuesta['paises'].append({
                "nombre_pais": pais,
                "promedio_salario": info['salario_promedio'],
                "total_empresas": len(info['empresas']),
                "total_ofertas": info['total_ofertas'],
                "total_ofertas_rango_salarial": sum(1 for oferta in ofertas_filtradas if oferta['pais'] == pais and oferta['tipo_salario'] == 'rango'),
                "total_ofertas_valor_fijo": sum(1 for oferta in ofertas_filtradas if oferta['pais'] == pais and oferta['tipo_salario'] == 'valor_fijo'),
                "total_ofertas_sin_salario": sum(1 for oferta in ofertas_filtradas if oferta['pais'] == pais and oferta['tipo_salario'] == 'sin_salario'),
                "habilidades_promedio": len(info['habilidades']) / info['total_ofertas']
            })
    
    # Aquí se debe completar la lógica para calcular el país con mayor y menor oferta salarial.
    # Esto requiere un análisis adicional de las ofertas filtradas por país y nivel de experiencia.
    
    return respuesta



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
    return sa.sort(list, cmp)
    
