"""Escribe un programa que calcule el promedio general de una clase."""


#Pedimos al usuario que ingrese la cantidad de alumnos
alumnos = int(input("Ingrese la cantidad de alumnos: "))

#Creamos listas vacía para almacenar los datos de las personas
suma = 0
contador = 0

##Pedimos al programa que repita el pedido de datos la cantidad de veces solicitada, además de realizar los cálculos necesarios
while contador < alumnos:
    nota = float(input("Ingrese la nota del alumno: "))
    suma += nota
    contador += 1

promedio_general = suma / alumnos

#Mostramos el promedio general por pantalla
print("El promedio general de la clase es:", promedio_general)