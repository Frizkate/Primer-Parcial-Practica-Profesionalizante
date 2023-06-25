"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)."""


#Se pide al usuario que ingrese los datos
cotizacion = int(input("¿A cuánto cotiza el dólar?: "))
dolar = int(input("¿Cuántos dólares tiene?: "))

#Cálculo de los valores ingresados
resultado = dolar * cotizacion

#Se muestran en pantalla la equivalencia a pesos de los dólares ingresados
print("Usted tiene ", resultado, "pesos")