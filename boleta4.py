#input
cliente=input("ingrese el nombre del cliente:")
numero_de_cuadernos=int(input("ingrese el numero de cuadernos:"))
precio_de_cuaderno=float(input("precio de un cuaderno:"))

#processing
costo_cuaderno=(numero_de_cuadernos*precio_de_cuaderno)

#verificador
padre_endeudado=(costo_cuaderno>=60)

#output
print("###################################")
print("#        BOLETA   DE    VENTA")
print("###################################")
print("#")
print("#cliente:            ",cliente)
print("#precio de cuaderno:     ",precio_de_cuaderno)
print("#costo cuaderno:         ",costo_cuaderno)
print("####################################")
print("#¿el padre quedo endeudado?:    ",padre_endeudado)
