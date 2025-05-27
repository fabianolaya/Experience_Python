from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)

usuario = input("Dime tu nombre: ")


print(f"bueno {usuario}, he pensado un numero entre 1 y 100\n tienes 8 inentos para adivinar")

while intentos < 8 :
    estimado = int(input("Cual es el numero?: "))
    intentos +=1

    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el ranfo de 1 a 100")
    elif estimado < numero_secreto:
        print("Mi numero es mas alto ")

    elif estimado > numero_secreto:
        print("mi numero es mas bajo ")

    else :
        print(f"Felicitaciones {usuario}! has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"lo siento, se han agotado los intentos. el numero secreto era {numero_secreto} ")