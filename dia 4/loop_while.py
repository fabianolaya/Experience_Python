moneda = 5

while moneda > 0:
    print(f"tengo {moneda} monedas")
    moneda = moneda - 1
else:
    print (f"no tengo mas dinero")

respuesta = 's'

while respuesta == 's':
    respuesta= input("quieres seguir (s/n")
else:
    print("gracias")

nombre = input ("Tu nombre: ")
for letra in nombre:
    if letra =='b':
        continue
    print(letra)

numero = 10

while numero < 10:
    numero -= 1
    print(f"numero {numero}")