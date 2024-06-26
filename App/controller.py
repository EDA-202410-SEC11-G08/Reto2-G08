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

Route = "small-"

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
    

# Funciones para la carga de datos ---------------------------------------------------------------------------------

def load_data(control, memflag = True):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalog = control['model']
    
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()

    load_data_jobs(catalog)
    #load_data_skills(catalog)
    #load_data_employment(catalog)
    #load_data_multilocation(catalog)
    
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
    
  
def load_data_jobs(catalog):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = cf.data_dir+ 'data/' + Route + 'jobs.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), restval= 'Desconocido', delimiter= ";")
    for row in input_file:
        model.add_data_jobs(catalog, row)
    catalog['Trabajos'] = model.sort(catalog['Trabajos'], model.cmp_fecha_empresa)
    
    
            

def load_data_skills(catalog):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = cf.data_dir + Route + 'skills.csv'
    input_file =csv.DictReader(open(file, encoding='utf-8'), restval= 'Desconocido', delimiter= ";", fieldnames = ['name','level','id'])
    for row in input_file:
        model.add_data_skills(catalog, row)   

def load_data_employment(catalog):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = cf.data_dir + Route + 'employments_types.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), restval= 'Desconocido', delimiter= ";", fieldnames = ['type','id','currency','salary_from', 'salary_to'])
    for row in input_file:
        model.add_data_employment_types(catalog, row)

def load_data_multilocation(catalog):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = cf.data_dir + Route + 'multilocations.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'), restval= 'Desconocido', delimiter= ";", fieldnames = ['city','street','id'])
    for row in input_file:
        model.add_data_jobs(catalog, row)    

def setDataSize(SizeOp):
    """
    Configura que csv se utilizara para la carga de datos
    """
    ans = model.selectDataSize(SizeOp)
    DataSize = ans[0]
    data_msg = ans[1]
    return data_msg, DataSize

# Funciones de ordenamiento ------------------------------------------------------------------------------------------

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo -----------------------------------------------------------------------------

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def set_country_experience(control, pais, experiencia, memflag = True): # REQUERIMIENTO 1 -------------------------------------------------
    """
    Retorna el resultado del requerimiento 1
    Ingresar catalogo, pais, experiencia
    """
    # TODO: Modificar el requerimiento 1

    jobs = control["model"]
    # Inicio de mediciones
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    ans = model.sort_country_experience(jobs, pais, experiencia)
    control["model"] = ans[0]
    size = ans[1] 
    
    # Finalización de mediciones
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return control, size, deltaTime, deltaMemory

    else:
        # respuesta sin medir memoria
        return control, size, deltaTime

def set_company_city(control, empresa, ciudad, memflag = True): # REQUERIMIENTO 2 ----------------------------------
    """
    Retorna el resultado del requerimiento 2
    Ingresar catalogo, empresa y ciudad
    """
    # TODO: Modificar el requerimiento 2
    jobs = control["model"]
    # Inicio de mediciones
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
        
    ans = model.sort_company_city(jobs, empresa, ciudad)
    control["model"] = ans[0]
    size = ans[1] 
    
    # Finalización de mediciones
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
        # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return control, size, deltaTime, deltaMemory

    else:
        # respuesta sin medir memoria
        return control, size, deltaTime

# Función para obtener las ofertas de trabajo por empresa y fecha del modelo # REQUERIMIENTO 3 ----------------------------------
def get_jobs_by_company_and_date(control, company_name, start_date, end_date):
    """
    Obtiene las ofertas de trabajo por empresa y fecha del modelo
    """
    # Llamar a la función correspondiente en el modelo
    return model.filter_jobs_by_company_and_date(control['model'], company_name, start_date, end_date)



def req_4(control,codigo_pais,fecha1,fecha2):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    res= model.req4(control["model"],codigo_pais,fecha1,fecha2)
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    return res,deltaTime


def set_city_date(control, ciudad, fecha1, fecha2, memflag=True): # REQUERIMIENTO 5 ----------------------------------------------------------------------
    """
    Retorna el resultado del requerimiento 5
    Ingresar catalogo, ciudad a investigar, fecha inicial (1) y fecha final (2)
    """
    # TODO: Modificar el requerimiento 5
    jobs = control["model"]
    # Inicio de mediciones
    start_time = get_time()
    if memflag is True:
        tracemalloc.start()
        start_memory = get_memory()
    
    ans = model.sort_city_date(jobs, ciudad, fecha1, fecha2)
        
    control["model"] = ans[0]
    size = ans[1] 
    max, min = ans[2], ans[3]
    
    # Finalización de mediciones
    stop_time = get_time()
    deltaTime = delta_time(start_time, stop_time)
    
    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = get_memory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        deltaMemory = delta_memory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return control, size, max, min, deltaTime, deltaMemory

    else:
        # respuesta sin medir memoria
        return control, size, max, min, deltaTime
     
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

def jobs_id_size(control):
    """
    Numero de id de ofertas en el catalogo
    """
    return model.jobs_id_size(control['model'])

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
