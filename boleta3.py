#input
cliente=input("ingre el nombre del cliente:")
numero_de_cajas_de_cerveza=int(input("ingrese el numero de cajas de cerveza:"))
precio_de_caja_de_cerveza=float(input("precio de una caja de cerveza:"))
#processing
costo_de_caja_de_cerveza=(numero_de_cajas_de_cerveza*precio_de_caja_de_cerveza)

#verificador
cliente_borracho=(costo_de_caja_de_cerveza>=80)

#output
print("################################")
print("#         BOLETA    DE     VENTA")
print("################################")
print("#")
print("#cliente:          ",cliente)
print("precio de caja de cerveza:    ",precio_de_caja_de_cerveza)
print("costo de caja de cerveza:     ",costo_de_caja_de_cerveza)
print("#################################")
print("#¿el cliente quedo borracho?:    ",cliente_borracho)
