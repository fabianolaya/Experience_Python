'''def suma ():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1 + n2)
    print('Gracias por sumar' + n1)



try:
    suma()
except TypeError:
    print("Esas intentando concatenar tipos de datos distintos ")
except ValueError:
    print("Ese no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")'''

'''def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()'''

def suma(num1,num2):
    try:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        Resultado = num1 + num2
    except:
        print("Error inesperado")
    else:
        print(Resultado)

suma(num1,num2)



