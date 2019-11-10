#input
cliente=input("ingrese el nombre del cliente:")
numero_de_helados=int(input("ingrese el numero de helados:"))
precio_de_helado=float(input("precio de un helado:"))

#processing
costo_helado=(numero_de_helados*precio_de_helado)

#verificador
cliente_con_gripe=(costo_helado>=15)

#output
print("###############################")
print("#       BOLETA    DE     VENTA")
print("###################################")
print("#")
print("#cliente:      ",cliente)
print("#precio de helado:       ",precio_de_helado)
print("#costo helado:     ",costo_helado)
print("##################################")
print("#el cliente quedo con gripe:    ",cliente_con_gripe)
