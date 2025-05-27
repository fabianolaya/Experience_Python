palabra = "python"

lista = [letra for letra in palabra]
print(lista)

listado = [n for n in range(0,21,2)]
print (listado)

#lista = [n / 2 for n in range (0,21,2)]
#print (lista)

listas = [n for n in range (0,21,2) if n * 2 > 10]
print (listas)

lis = [n if n * 2 > 10 else 'no' for n in range (0,21,2)]
print(lis)

pies = [10,20,30,40,50]
metros =[p * 3.281 for p in pies]

print (metros)
