"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    
    control= controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control, memflag):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    ans = controller.load_data(control, memflag)
    return ans


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(list, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    table = []
    header = ['Publicación','País','Ciudad','Empresa','Oferta','Experticia','Formato de aplicación','Tipo']
    table.append(header)
    if lt.size(list) <= num:
        jobs = list
    else: jobs = lt.subList(list, 1, num)
 

    for job in lt.iterator(jobs):
        table.append([job['published_at'],
        job['country_code'],
        job['city'],
        job['company_name'],
        job['title'],
        job['experience_level'],
        job['company_url'],
        job['workplace_type']])
        
    return table


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(list, num):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    table1 = []
    table2 = []
    header = ['Publicación','Oferta','Empresa','Tamaño','Ubicación']
    table1.append(header)
    table2.append(header)
    jobs1 = lt.subList(list, 1, num)
    jobs2 = lt.subList(list, lt.size(list)-num+1, num)

    for job in lt.iterator(jobs1):
        table1.append([job['published_at'],
        job['title'],
        job['company_name'],
        job['company_size'],
        job['workplace_type']])  

    for job in lt.iterator(jobs2):
        table2.append([job['published_at'],
        job['title'],
        job['company_name'],
        job['company_size'],
        job['workplace_type']])      
        
    return table1, table2


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def printTableJobs(list, num):
    table1 = []
    table2 = []
    header = ['Oferta','Empresa','Experticia','Publicación','País','Ciudad']
    table1.append(header)
    table2.append(header)
    jobs1 = lt.subList(list, 1, num)
    jobs2 = lt.subList(list, lt.size(list)-num+1, num)

    for job in lt.iterator(jobs1):
        table1.append([job['title'],
        job['company_name'],
        job['experience_level'],
        job['published_at'],
        job['country_code'],
        job['city']])

    for job in lt.iterator(jobs2):
        table2.append([job['title'],
        job['company_name'],
        job['experience_level'],
        job['published_at'],
        job['country_code'],
        job['city']])
        
    return table1, table2

def printLoadDataAnswer(answer):
    """
    Imprime los datos de tiempo y memoria de la carga de datos
    """
    if isinstance(answer, (list, tuple)) is True:
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "||",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    else:
        print("Tiempo [ms]: ", f"{answer:.3f}")
        
def castBoolean(value):
    """
    Convierte un valor a booleano
    """
    if value in ('True', 'true', 'TRUE', 'T', 't', '1', True):
        return True
    else:
        return False

# Se crea el controlador asociado a la vista
control = new_controller()
# Variables utiles para el programa
SizeOpStr = """Seleccione el tamaño de CSV a cargar:
                 1. 10-por ||
                 2. 20-por ||
                 3. 30-por ||
                 4. 40-por ||
                 5. 50-por ||
                 6. 60-por ||
                 7. 70-por ||
                 8. 80-por ||
                 9. 90-por ||
                 10. small ||
                 11. medium||
                 12. large ||
                 """     
Req1OP = """Seleccione un nivel de experiencia
                junior
                mid
                senior
"""
# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1: # CARGA DE DATOS ------------------------------------------------------
            print("Cargando información de los archivos ....\n")
            # Definir que archivos csv se van a utilizar para cargar datos -------------------------
            print("Que datos desea cargar?\n")
            SizeOp = input(SizeOpStr)
            SizeOp = int(SizeOp)
            Sizemsg, DataSize = controller.setDataSize(SizeOp)      
            controller.Route = DataSize    
            print(Sizemsg) 
            # Observar uso de memoria en la carga de datos ----------------------------------------
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            # Ejecutar comando de cargar datos
            ans = load_data(control, memflag=mem)
            printLoadDataAnswer(ans)
            # Cantidad de datos guardados ---------------------------------------------------------
            print('Ofertas cargadas: ' + str(controller.jobs_id_size(control))) 
            #print('Libros cargados: ' + str(controller.skills_size(control))) 
            #print('Libros cargados: ' + str(controller.employment_size(control))) 
            #print('Libros cargados: ' + str(controller.multilocation_size(control))) 
            # Ofertas a visualizar
            num = input('Cuantas ofertas desea visualizar ')
            table1, table2 = printTableJobs(control["model"]["Trabajos"], int(num))
            print('Primeras ' + str(num) + " Ofertas")
            print(tabulate(table1))
            print('Ultimas ' + str(num) + " Ofertas")
            print(tabulate(table2))
        
        elif int(inputs) == 2: # REQUERIMIENTO 1 --------------------------------------------------------------------
            
            num = input('Cuantas ofertas desea visualizar ')            
            pais = input('Por cúal país desea filtrar?\nIngresar código de país\n')
            experiencia = input (Req1OP)
            ans = controller.set_country_experience(control, pais, experiencia, memflag = mem)
            control = ans[0]
            req1size = ans[1]
            DeltaTime = f"{ans[2]:.3f}"         

            if req1size == 0:
                print("País o experiencia invalido")
            else: 
                
                
                print("Tiempo [ms]: ", f"{ans[2]:.3f}")
                if (mem == True): print("Memoria [kB]: ", f"{ans[3]:.3f}")    
                                
                print("Se filtraron y organizaron", req1size, "ofertas")                
                table = print_req_2(control['model']['REQ1'], int(num))             
                print('Ultimas ' + str(req1size) + " Ofertas")
                print(tabulate(table))   
                
        elif int(inputs) == 3: # REQUERIMIENTO 2 --------------------------------------------------------------------
            
            num = input('Cuantas ofertas desea visualizar ')
            empresa = input('Cúal empresa desea filtrar?\n')
            ciudad = input('Cúal ciudad desea filtrar?\n')
            
            ans = controller.set_company_city(control, empresa, ciudad, memflag=mem)
            control = ans[0]
            req2size = ans[1]

            if req2size == 0:
                print("Empresa o ciudad invalida")
            else:
                print("Tiempo [ms]: ", f"{ans[2]:.3f}")
                if (mem == True): print("Memoria [kB]: ", f"{ans[3]:.3f}")    
                                
                print("Se filtraron y organizaron", req2size, "ofertas")                
                table = print_req_2(control['model']['REQ2'], int(num))             
                print('Ultimas ' + str(num) + " Ofertas")
                print(tabulate(table))    
                
        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6: # REQUERIMIENTO 5 ----------------------------------------------------------------
                   
            ciudad = input("Que ciudad desea consultar?\n")
            fecha1 = input("En que fecha desea iniciar? formato YYYY-MM-DD\n")
            fecha2 = input("En que fecha desea terminar? formato YYYY-MM-DD\n")
            # Observar uso de memoria en la carga de datos ----------------------------------------
            print("Desea observar el uso de memoria? (True/False)")
            mem = input("Respuesta: ")
            mem = castBoolean(mem)
            
            ans = controller.set_city_date(control, ciudad, fecha1, fecha2, memflag=mem) #FILTRADO Y ORGANIZAR
            
            control = ans[0]
            req5size = ans[1]
            maxreq5, minreq5 = ans[2], ans[3]
            DeltaTime = f"{ans[4]:.3f}"  
                    
            if req5size == 0: #Si la lista regresa vacia, hubo problemas de filtrado
                print("Ciudad o fechas invalidas")   
            else:
                
                print("Tiempo [ms]: ", f"{ans[4]:.3f}")
                if (mem == True): print("Memoria [kB]: ", f"{ans[5]:.3f}")                
                print("Se encontraron", req5size,"ofertas entre las fechas", fecha1,"y",fecha2)
                print("La empresa con mayor ofertas es",maxreq5[0],"con",str(maxreq5[1]),"ofertas")
                print("La empresa con menor ofertas es",minreq5[0],"con",str(minreq5[1]),"ofertas")
                
                num = input('Cuantas ofertas desea visualizar ')
                table1, table2 = print_req_5(control['model']['REQ5'], int(num))             
                print('Primeras ' + str(num) + " Ofertas")
                print(tabulate(table1))
                print('Ultimas ' + str(num) + " Ofertas")
                print(tabulate(table2))
            
        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
