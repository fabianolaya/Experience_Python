nombres = ['fabian','mateo','isis',]
edades = [30,28,12,]
ciudades = ['bogota','mexico','argentina']

combinados = list(zip(nombres,edades,ciudades))



for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

#creacion de un zip con una lista dividiendo los numeros en idiomas
español = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(español, portugues, ingles))  # Combina las listas en un objeto zip y lo convierte en lista

print(numeros)