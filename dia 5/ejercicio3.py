def argumentos(*args):
    for i in range(len(args) - 1):

        if args[i] == 0 and args[i + 1] == 0:
            return True

    return False

print(argumentos(2,4,3,1,0,9,0,0))
print(argumentos(3,3,4,0,0,8,0,8))

def ceros_vecinos(*args):

    contador = 0

    for num in args:
        if args[contador] == 0 and args[contador + 1] ==0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(3,4,5,6,7,8,9,0,0,23,3,1))