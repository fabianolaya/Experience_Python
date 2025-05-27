num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"el {num2} no es mayor a el {num1}")
else:
    print(f"el {num1} y {num2} son iguales")