producto = input("Escriba el nombre del producto")
precio = input("Introduzca el precio del producto")
cantidad = int(input("Introduce el número de unidades que ha cogido"))
precio = precio.replace(",",".")
precio = round(float(precio),2)
preciototal = precio * cantidad
precio = "{:09.2f}".format(precio)
cantidad = "{:>03}".format(precio)
preciototal = "{:011.2f}".format(preciototal)
print("El producto es",producto+"\nEl precio es",precio+"\nLa cantidad es",cantidad+"\nY el precio final es",preciototal)