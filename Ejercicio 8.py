"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas."""


# Creamos una lista vacía para almacenar los datos de las personas
i = 0
#Pedimos al programa que repita cinco veces el pedido de los datos de cada persona y que lo muestre en pantalla
while i < 5:
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    print("Hola, ", nombre, " ", apellido, ". Usted tiene ", edad, " años.")
    i += 1