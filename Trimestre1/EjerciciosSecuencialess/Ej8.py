"""
8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero
obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
en cuenta su sueldo base y comisiones.
Fecha: 08/10/2022

Autor: Javier Postigo 
"""

print("Programa que calcula el sueldo de un comerciante basado en sus ventas y comisión por venta.")

# Petición de datos.
primera_venta = float(input("Dinero obtenido de la primera venta. "))
segunda_venta = float(input("Dinero obtenido de la segunda venta. "))
tercera_venta = float(input("Dinero obtenido de la tercera venta. "))

# Calculo
comision_primera = (primera_venta * 0.1)
comision_segunda = (segunda_venta * 0.1)
comision_tercera = (tercera_venta * 0.1)


print("Dinero obtenido de las comisiones: ", comision_primera + comision_segunda + comision_tercera)
print("Salario base sin comisiones", primera_venta + segunda_venta + tercera_venta)
print("Salario total: ", (primera_venta + comision_primera) + (segunda_venta + comision_segunda) + (tercera_venta
                                                                                                + comision_tercera))
