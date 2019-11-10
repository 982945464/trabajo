#input
cliente=input("ingrese el nombre del cliente:")
numero_de_zapatillas=int(input("inrese el numero de zapatillas:"))
precio_de_zapatilla=float(input("precio de cada zapatilla:"))

#processing
costo_zapatilla=(numero_de_zapatillas*precio_de_zapatilla)

#verificador
comprador_compulsivo=(costo_zapatilla>=400)

#output
print("#######################################")
print("#        BOLETA      DE      VENTA")
print("#######################################")
print("#")
print("#cliente:      ",cliente)
print("#precio de zapatillas:    ",precio_de_zapatilla)
print("#costo zapatilla:     ",costo_zapatilla)
print("#######################################")
print("#¿el comprador es compulsivo?:     ",comprador_compulsivo)
