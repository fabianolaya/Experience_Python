texto = input("Ingresa un texto a eleccion : ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print ("\n")
print ( "CANTIDAD DE LETRAS EN EL TEXTO : ")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print (f"Hemos enontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces ")
print (f"Hemos enontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces ")
print (f"Hemos enontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces ")

print ("\n")
print ("CANTIDAD DE PALBRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print ("\n")
print ("LETRAS DE INICIO Y DE FIN ")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"la letra de inicio es '{letra_inicio}' y la letra de final es '{letra_final}'")

print("\n")
print ("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print (f"Si ordenamos tu texto al reves va a decir '{texto_invertido}'")

print ("\n")
print ("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic ={True:'si',False:"no"}
print (f"La palabra 'python' {dic[buscar_python]} se encuetra en el texto")
