"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de personas ingresada por el usuario."""


#Pedimos al usuario que ingrese la cantidad de personas que quiera que el programa muestre sus datos
personas = int(input("Ingrese la cantidad de personas: "))

# Creamos una lista vacía para almacenar los datos de las personas
i = 0

#Pedimos al programa que repita cinco veces el pedido de los datos de cada persona y que lo muestre en pantalla
while i < personas:
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    print("Hola, ", nombre, " ", apellido, ". Usted tiene ", edad, " años.")
    i += 1