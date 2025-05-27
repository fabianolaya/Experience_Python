def devolver_distintos(num1,num2,num3):
    suma = num1+num2+num3
    numeros = sorted([num1,num2,num3])

    if suma > 15:
        return numeros[-1]
    elif suma < 10:
        return numeros[0]
    else:
        return numeros [1]

print(devolver_distintos(3,5,10))
print(devolver_distintos(12,4,8))
print(devolver_distintos(1,2,3))

def devolver_distintos(a,b,c):

    suma = a+b+c
    lista = [a,b,c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(7,2,4))



