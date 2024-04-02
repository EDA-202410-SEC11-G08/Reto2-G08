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
from datetime import datetime as date
assert cf



# Construccion de modelos


def new_catalog():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {'mapa_ids': None,
               'mapa_paises': None,
               'mapa_fechas': None,
               'mapa_ciudades': None,
               'habilidades_id': None,
               'habilidades_name': None,
               'Tipos': None,
               'Multi Locaciones': None,}
    
    catalog["mapa_ids"] = mp.newMap(60000,maptype="CHAINING",loadfactor=8) #Estructura para guardar los datos correspondientes a los ID's 
    catalog["mapa_paises"] = mp.newMap(390,maptype="PROBING") #Estructura para guardar los datos de los países
    catalog["mapa_fechas"] = mp.newMap(60000,maptype="CHAINING") #
    catalog["mapa_ciudades"] = mp.newMap(10000,maptype="CHAINING") #  
    catalog["habilidades_id"] = mp.newMap(10000,maptype="CHAINING") #  
    catalog["habilidades_name"] = mp.newMap(10000,maptype="CHAINING") #  

    return catalog


# Funciones para agregar informacion al modelo

def add_data_jobs(catalog, job):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos
    #IDs
    jobs_id = catalog['mapa_ids']
    idr = job['id']
        
    existid = mp.contains(jobs_id, idr)
    if existid:
        entry = mp.get(jobs_id, idr)
        id = me.getValue(entry)
    else:
        id = new_jobs_id(idr)
        mp.put(jobs_id, idr, id)
    lt.addLast(id['row'], job)
    
    """
    #Ofertas
    mp.put(mapa_dentro_id,"oferta",job)
    mp.put(ids,id_job,mapa_dentro_id)
    
    #Países
    paises=catalog["mapa_paises"]
    pais_job=job["country_code"]
    
    #Revisa que exista el país en el mapa de países. Si se obtiene que no existe (False), se crea
    if not mp.contains(paises,pais_job):
        mp.put(paises,pais_job,lt.newList("ARRAY_LIST"))
    mapi=mp.get(paises,pais_job)
    
    lista_paises=me.getValue(mapi)
    lt.addLast(lista_paises,job) 
    """   

def new_jobs_id(idr):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'id': "", "row": None}
    entry['id'] = idr
    entry['row'] = lt.newList('ARRAY_LIST')
    return entry    
           
    
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
    Numero de autores en el catalogo
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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
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


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
