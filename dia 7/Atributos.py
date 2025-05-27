class Pajaro:
    alas = True

    def  __init__(self,color,tamano):
        self.color = color
        self.tamano = tamano

mi_pajaro = Pajaro("Negro","grande")
print(f"Mi Pajaro es de color {mi_pajaro.color} y es de tamaño {mi_pajaro.tamano}")
print (mi_pajaro.alas)
print(Pajaro.alas)