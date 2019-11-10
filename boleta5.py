#input
cliente=input("ingrese el nombre del cliente:")
numero_de_chocolates=int(input("ingrese el numero de chocolates:"))
precio_de_chocolate=float(input("precio de un numero_de_chocolates:"))

#processing
costo_chocolate=(numero_de_chocolates*precio_de_chocolate)

#verificador
comprador_compulsivo=(costo_chocolate>=50)

#ouput
print("#################################")
print("#      BOLETA    DE    VENTA")
print("#################################")
print("#")
print("#cliente:         ",cliente)
print("#precio de chocolate:     ",precio_de_chocolate)
print("#costo chocolate:    ",costo_chocolate)
print("###################################")
print("#¿el comprador es compulsivo?:    ",comprador_compulsivo)
