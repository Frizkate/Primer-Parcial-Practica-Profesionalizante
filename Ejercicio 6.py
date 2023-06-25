"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13."""


#Pedimos al usuario que ingrese las horas trabajadas en el mes
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))

#Evaluamos los importes
if horas_trabajadas > 120:
    valor_hora = 1500
    bonificacion = 0.18
elif horas_trabajadas >= 80:
    valor_hora = 1300
    bonificacion = 0.15
else:
    valor_hora = 1100
    bonificacion = 0.13

#Calculamos las variables
sueldo_bruto = horas_trabajadas * valor_hora
monto_bonificacion = sueldo_bruto * bonificacion
sueldo_neto = sueldo_bruto + monto_bonificacion

#Mostramos los valores en pantalla
print("Sueldo Bruto: $", sueldo_bruto)
print("Monto a bonificar: $", monto_bonificacion)
print("Sueldo Neto: $", sueldo_neto)