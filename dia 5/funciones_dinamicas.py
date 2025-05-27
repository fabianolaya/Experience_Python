def chequear_3_cifras(numero):
    return numero in range(100,1000)


suma = 456 + 542
resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
         lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_3_cifras([555,67,800])
print(resultado)

