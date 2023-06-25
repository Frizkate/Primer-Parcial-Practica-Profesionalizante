"""Escribe un programa que calcule el área y el perímetro de un cuadrado y muestre los resultados por pantalla"""


#Pedimos al usuario que ingrese los datos
lado = float(input("Ingrese la longitud del lado del cuadrado: "))

#Cálculo de las variables
area = lado ** 2
perimetro = 4 * lado

#Se muestran los resultados en pantalla
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)