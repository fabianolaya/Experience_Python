def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10

print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))

def mis_generadores():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

h = mis_generadores()

print(next(h))
print(next(h))
print(next(h))


