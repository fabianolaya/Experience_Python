lista= ['a','b','c']

for indice,item in enumerate(range(50,56)):
    print(indice,item)

objetos = ['a','b','c']

mis_tuples = list(enumerate(objetos))
print(mis_tuples[0][1])

#revisar un indice de inicio de un nombre
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):  # Usa enumerate para obtener índices y nombres
    if nombre.startswith("M"):  # Verifica si el nombre empieza con "M"
        print(indice)


# #calcular el cuadrado de un numero en un rango de 1 a 15
suma_cuadrados = 0

for numero in range(1, 16):  # Crea un rango de 1 a 15 (inclusive)
    suma_cuadrados += numero ** 2  # Calcula el cuadrado y lo acumula

print(suma_cuadrados)


