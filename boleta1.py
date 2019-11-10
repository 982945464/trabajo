#imput
cliente=input("ingrese el nombre del cliente:")
numero_de_botellas_de_vino=int(input("ingrese el numero de las botellas:"))
precio_de_cada_vino=float(input("precio del vino:"))

#processing
precio_botella=(numero_de_botellas_de_vino*precio_de_cada_vino)

#verificador
comprador_compulsivo=(precio_botella<=50)

#output
print("############################")
print("  BOLETA DE VENTA ")
print("#")
print("#cliente     :",cliente)
print("#precio de cada vino     :",precio_de_cada_vino)
print("#precio por botella  :",precio_botella)
print("#############################")
print("¿comprador compulsivo?   :",comprador_compulsivo)
