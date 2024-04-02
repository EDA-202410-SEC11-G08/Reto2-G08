﻿"""
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
 """

import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

csv.field_size_limit(2147483647)

def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos - DONE

    control = {
        'model': None
    }
    control['model'] = model.new_catalog()
    return control    
    

# Funciones para la carga de datos

def load_data(control, filename, memflag = True):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()

    jobs=open(filename+"-jobs.csv",encoding="utf-8")
    load_data_jobs(control,jobs)

    """
    skills=open(filename+"-skills.csv",encoding="utf-8")
    load_data_skills(control,skills)
    
    employment_type=open(filename+"-employments_types.csv",encoding="utf-8")
    load_data_employment(control,employment_type)
    
    multilocation=open(filename+"-multilocations.csv",encoding="utf-8")
    load_data_multilocation(control,multilocation)
    """
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return deltaTime, deltaMemory

    else:
        # respuesta sin medir memoria
        return deltaTime
    
  
def load_data_jobs(control, jobs):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    lectura=csv.DictReader(jobs,delimiter=";")
    lectura.__next__()
    for i in lectura:
        model.add_data_jobs(control['model'], i)
            

def load_data_skills(control, skills):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    lectura=csv.DictReader(skills, restval= 'Desconocido', delimiter= ";", fieldnames = ['name','level','id'])
    for i in lectura:
        model.add_data_skills(control['model'], i)    

def load_data_employment(control, employment_type):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    lectura=csv.DictReader(employment_type)
    for i in lectura:
        model.add_data_employment_types(control, i) 
                


def load_data_multilocation(control, multilocation):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    lectura= csv.DictReader(multilocation)
    for i in lectura:
        model.add_data_multilocation(control,i)
    
def jobs_id_size(control):
    """
    Numero de libros cargados al catalogo
    """
    return model.jobs_id_size(control['model'])

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
