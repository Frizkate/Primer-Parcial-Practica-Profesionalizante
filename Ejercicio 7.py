"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas, escribe un programa que calcule el descuento anual a realizarse, considerando:a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual a descontarse y las horas trabajadas en todo el año."""


#Pedimos al usuario que ingrese la cantidad de horas trabajadas por mes
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas por mes: "))

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
horas_anuales = horas_trabajadas * 12
sueldo_bruto_anual = horas_anuales * valor_hora
monto_bonificacion_anual = sueldo_bruto_anual * bonificacion

#Establecemos las condicionales para los descuentos
if sueldo_bruto_anual > 2000000:
    descuento_anual = sueldo_bruto_anual * 0.05
elif sueldo_bruto_anual >= 1000000:
    descuento_anual = sueldo_bruto_anual * 0.03
else:
    descuento_anual = sueldo_bruto_anual * 0.01

#Cálculo del sueldo neto anual
sueldo_neto_anual = sueldo_bruto_anual + monto_bonificacion_anual - descuento_anual

#Mostramos los valores en pantalla
print("Horas trabajadas anuales:", horas_anuales)
print("Sueldo bruto anual: $", sueldo_bruto_anual)
print("Monto anual de bonificaciones: $", monto_bonificacion_anual)
print("Monto anual a descontar: $", descuento_anual)
print("Sueldo neto anual: $", sueldo_neto_anual)