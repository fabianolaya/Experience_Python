from random import *

aleatorio = round(uniform(1,5),1)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['morado','azul','gris','rojo','amarillo']
aleatorio = choice(colores)
print(aleatorio )

numeros = list(range(5,50,5))

shuffle(numeros)

print (numeros)

num1 = int(input("ingresa el primer numero"))  # Solicita el primer número
num2 = int(input("Ingresa el segundo numero"))  # Solicita el segundo número

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"el {num2}es mayor que {num1}")


