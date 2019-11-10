#input
cliente=input("ingrese el nombre del cliente:")
numero_de_polos=int(input("ingrese el numero de polos:"))
precio_de_polo=float(input("precio de cada polo:"))

#processing
costo_polo=(numero_de_polos*precio_de_polo)

#verificador
cliente_endeudado=(costo_polo>=60)

#output
print("##################################")
print("#        BOLETA     DE      VENTA")
print("###################################")
print("#")
print("#cliente:       ",cliente)
print("#precio de polo:      ",precio_de_polo)
print("#costo polo:        ",costo_polo)
print("##################################")
print("#¿el cliente quedo endeudado?: ",cliente_endeudado)
