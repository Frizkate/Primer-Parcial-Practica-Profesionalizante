"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas."""


#Iniciamos los contadores de personas ingresadas y sus edades, asi como le damos el valor a la variable "continuar" que permita que siga pidiendo datos
suma_edades = 0
contador = 0
continuar = 1

#El programa pide al usuario que ingrese una edad válida para incrementar el contador de edades y personas ingresadas. Caso contrario, debe ingresar "fin" para terminar el proceso
while continuar == 1:
    edad = input("Ingrese una edad (o 'fin' para terminar): ")
    if edad.lower() == "fin":
        continuar = 0
    else:
        suma_edades += int(edad)
        contador += 1

#Calculamos el promedio
promedio_edades = suma_edades / contador

#Mostramos la informacion solicitada en pantalla
print("El promedio de edades ingresadas es: ", promedio_edades)
print("Total de personas ingresadas: ", contador)