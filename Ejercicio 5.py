"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente:
a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100."""


#Pedimos al usuario que ingrese las horas trabajadas en el mes
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))

#Evaluamos los importes
if horas_trabajadas > 120: 
    valor_hora = 1500
elif horas_trabajadas >= 80:
    valor_hora = 1300
else:
    valor_hora = 1100

#Calculamos sueldo
sueldo = horas_trabajadas * valor_hora

#Mostramos los valores en pantalla
print("El sueldo del empleado es: $", sueldo)