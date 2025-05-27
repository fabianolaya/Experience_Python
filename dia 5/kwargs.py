def prueba (num1, num2, *args,**kwargs):

    print(f"El primer  valor e {num1}")
    print(f"El segundo valor e {num2}")

    for arg in args:
        print(f"args = {arg}")

    for clave,valor  in kwargs.items():
        print(f"{clave} = {valor}")


args = [ 67,56]
kwargs = {'x':'uno','y':'dos', 'z':'tres'}
prueba(12,4,*args,**kwargs)

