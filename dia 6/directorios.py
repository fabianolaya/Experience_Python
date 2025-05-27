import os

#ruta = 'C:\\Users\\FabianPC\\Desktop\\Python\\pythonProject1\\dia 6\\prueba.txt'

#elemento = os.path.dirname(ruta)
#elemento = os.path.split(ruta)

#os.rmdir('C:\\Users\\FabianPC\\Desktop\\otra')

#otro_archivo = open('C:\\Users\\FabianPC\\Desktop\\Python\\pythonProject1\\dia 6\\prueba1.txt')
#print (otro_archivo.read())

from Opcion_lib import Path

carpeta = Path('C://Users//FabianPC//Desktop//Pytho//npythonProject1//dia 6')
archivo = carpeta / 'prueba1.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

