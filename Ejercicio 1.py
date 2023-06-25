"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento."""


#Pedimos al usuario que ingrese los datos
anonacimiento = int(input("Ingrese el año de su nacimiento: "))

#Cálculo de la variable "edad"
edad = 2023 - anonacimiento

#Se muestra en pantalla la edad
print("Usted cumplió o cumplirá", edad, "años en el 2023.")