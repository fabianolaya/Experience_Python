diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)
resultado = diccionario['c1']
print(resultado)

cliente= {'nombre':'fabian','apellido':'Olaya','edad':29,'sexo':'Masculino','talla':1.76}
consulta = (cliente['apellido'])
print (consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print (dic['c3']['s2'])

dic1 = {'c1':['a','b','c'],'c2':['d','e','f']}
letra = dic1['c2'][1]

print(letra.upper())

dic2 = {1:'a',2:'b'}
print(dic2)

dic2[3] = 'c'
dic2[4] = 'd'
dic2[2] = 'B'
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items())
