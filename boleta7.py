#input
cliente=input("ingrese el nombre del cliente:")
numero_de_cremoladas=int(input("ingrese el numero de cremoladas:"))
precio_de_cremolada=float(input("precio de una cremolada:"))

#processing
costo_cremolada=(numero_de_cremoladas*precio_de_cremolada)

#verificador
limite=(costo_cremolada>=40)

#output
print("#####################################")
print("#      BOLETA    DE    VENTA")
print("######################################")
print("#")
print("#cliente:      ",cliente)
print("#precio de cremoladas:      ",precio_de_cremolada)
print("#costo cremolada:      ",costo_cremolada)
print("#######################################")
print("#el precio paso el limite establecido:    ",limite)
