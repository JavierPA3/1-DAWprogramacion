"""
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central,
América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la
que va dirigido. Lo anterior se muestra en la tabla:

ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones
de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

Fecha: 21/10/2022
Autor: Javier Postigo

"""

peso_paquete = float(input("¿Cuántos gramos pesa el paquete? "))

if peso_paquete / 1000 < 5:
    ubicacion_entrega_paquete = input("¿A que continente desea llevar el paquete? ")
    if ubicacion_entrega_paquete.upper() == 'AMERICA DEL NORTE':
        print("El coste va a ser de:", peso_paquete * 24, "€.")
    elif ubicacion_entrega_paquete.upper() == 'AMERICA CENTRAL':
        print("El coste va a ser de:", peso_paquete * 20, "€.")
    elif ubicacion_entrega_paquete.upper() == 'AMERICA DEL SUR':
        print("El coste va a ser de:", peso_paquete * 21, "€.")
    elif ubicacion_entrega_paquete.upper() == 'EUROPA':
        print("El coste va a ser de:", peso_paquete * 10, "€.")
    elif ubicacion_entrega_paquete.upper() == 'ASIA':
        print("El coste va a ser de:", peso_paquete * 18, "€.")
else:
    print("Pesa más de 5kg, por cuestiones de logística y seguridad no podemos transportar el pedido. ")
