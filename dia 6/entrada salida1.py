
mi_archivo = open('prueba.txt')

#una_linea = mi_archivo.readline()
#print(una_linea.upper())

#una_linea = mi_archivo.readline()
#print(una_linea.rstrip()) #.rstrip hace que en la ejecucion del codigo no parezcan saltos de linea

#una_linea = mi_archivo.readline()
#print(una_linea)


#mi_archivo.close() #cerrar el archivo

#for l in mi_archivo:
    #print('Aque dice: '+ l)

todas = mi_archivo.readlines()

todas= todas.pop()
print(todas)