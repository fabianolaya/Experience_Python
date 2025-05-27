lista = ['fabian ','carolina ','mateo ','isis','martha']

for nombre in lista:
    if nombre.startswith('m'):
        print (nombre)
    else:
        print('no se encuentra ningun nombre')

lista_numeros = [1,2,3,4,5]
mi_valor = 0
for numero in lista_numeros:
    mi_valor = mi_valor + numero

print (mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print (a)
    print (b)

dic = {'clave1':'a','clave2:':'b','clave3':'c'}

for item in dic.items():
     print(item)









