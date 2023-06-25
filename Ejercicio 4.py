"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)."""


#Pedimos al usuario que ingrese las notas
num1 = float(input("Ingrese la primer nota: "))
num2 = float(input("Ingrese la segunda nota: "))
num3 = float(input("Ingrese la tercer nota: "))

#Calculamos el promedio
resultado = (num1 + num2 + num3) / 3

#Mostramos los resultados en pantalla
if resultado<6:
    print("Usted ha desaprobado la materia. Debe recursar.")
elif resultado>6:
    print("Usted ha aprobado la materia. Felicidades!")