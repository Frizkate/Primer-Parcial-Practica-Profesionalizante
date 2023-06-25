"""Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
    a. Si es número es par o impar.
    b. Cuanto es la suma total de todos los números mostrados.
    c. Cuanto es la suma total de todos los números pares mostrados.
    d. Cuanto es la suma total de todos los números impares mostrados."""


#Creamos contadores para que el programa lleve registro de los números y de sus posteriores sumas
numero = 1
total = 0
pares = 0
impares = 0

#Iniciamos el repetidor que contará los números y los diferencia para mencionarlos en pantalla y posicionarlos en sus correspondientes casillas de suma
while numero <= 10:
    total += numero
    if numero % 2 == 0:
        tipo = "par"
        pares += numero
    else:
        tipo = "impar"
        impares += numero
    print(numero, "es", tipo)

    numero += 1

#Mostramos en pantalla los resultados de las sumas
print("La suma total es:", total)
print("La suma de los pares es:", pares)
print("La suma de los impares es:", impares)