nombre = input("Dime tu nombre: ")
ventas = input("Dime tus ventas durante el mes: ")

ventas = int(ventas)  #conversion de string a int

comision = ventas * 13 / 100
comision = round(comision,2)

print (f"Hola {nombre}, tus comisiones de este mes son de ${comision}")




