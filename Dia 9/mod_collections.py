from collections import *

#metodo counter
# serie = Counter([1,1,2,2,3,3,2,2,1,2,4,7,9,0,8,7,6,6,5,6,4,5,5,3,4,5])
#numeros = Counter(serie)
#print(numeros)
# print(serie.most_common(3))
# print((list(serie))


# metodo defaultdic
# mi_dic = {'uno':'verde','dos':'azul','tres':'rojo'}
# print(mi_dic['dos'])

#mi_dic = defaultdict(lambda :'nada')
#mi_dic['uno'] = 'verd'
#mi_dic['dos'] = 'azul'

#print(mi_dic['tres'])
#print(mi_dic)

Persona = namedtuple('Persona',['nombre','altura','peso'])
fabian = Persona('Fabian',1.84,70)

print(fabian.peso)