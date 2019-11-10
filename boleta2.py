#input
cliente=input("ingrese el nombre del cliente:")
numero_de_empanadas=int(input("ingrese el numero de empanadas:"))
precio_de_empanada=float(input("precio de una empanada:"))

#processing
costo_empanada=(numero_de_empanadas*precio_de_empanada)

#verificador
cliente_hambriento=(costo_empanada>=20)

#output
print("###################################")
print("#              BOLETA     DE    VENTA")
print("###################################")
print("#")
print("#cliente:      ",cliente)
print("#precio de empanada:      ",precio_de_empanada)
print("#costo empanada:         ",costo_empanada)
print("####################################")
print("#¿el cliente es hambriento?:    ",cliente_hambriento)
