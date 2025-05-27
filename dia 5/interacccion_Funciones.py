from random import *

#lista inicial
palitos = ['-','--','---','----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return(lista)

#pedire el intento
def probar_suerte():
    intentos = ''

    while intentos not in ['1','2','3','4']:
        intentos = input ("Elige un numero del 1 al 4: ")

    return int(intentos)

#comprobar intento
def chequear_intento(lista,intentos):
    if lista [intentos -1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez no te ha tocado")

    print(f"te ha tocado {lista[intentos-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

import random


def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])


def probar_suerte(resultado_lanzamiento, lista):
    if resultado_lanzamiento == "Cara":
        print("La lista se autodestruira ")
        return []
    else:
        print("La lista fue salvada")
        return lista


lista_numeros = [3, 5, 8, 12, 7]
resultado = lanzar_moneda()
print(f"Resultado del lanzamiento:  {resultado}")
lista_final = probar_suerte(resultado, lista_numeros)
print("Lista final: ,{lista_final}")