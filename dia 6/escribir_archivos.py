archivo = open ('prueba1.txt', 'w')
archivo.write ('''soy el nuevo texto
como 
estas el dia de hoy ''')
lista = ['hola','mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p +'\n')


archivo.close()

archivo = open ('prueba1.txt', 'a')
archivo.write ('Bienvenido')