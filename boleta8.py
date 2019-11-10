#input
consultora=input("ingrese el nombre de la consultora:")
numeros_de_productos=int(input("ingrese el numero de productos:"))
precio_del_producto=float(input("precio de cada producto:"))

#processing
costo_producto=(numeros_de_productos*precio_del_producto)

#verificador
costo_excesico=(costo_producto>=80)

#output
print("################################")
print("#       BOLETA     DE     VENTA")
print("################################")
print("#")
print("#consultora:       ",consultora)
print("#precio de productos:      ",precio_del_producto)
print("#costo producto:       ",costo_producto)
print("#################################")
print("#¿el costo es excesivo?:     ",costo_excesico)
