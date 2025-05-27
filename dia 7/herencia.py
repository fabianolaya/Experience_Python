class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super.__init__(edad,color)
        self.altura_vuelo = altura_vuelo


    def hablar(self):
        print('pio')

    def volar(self,metros):
        print(f" EL pajaro vuela {metros} metros")





mi_animal = Animal(5,'negro')






class Padre:
    def habla(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja ')

    def habla(self):
        print('que tal')

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo ):
    pass


mi_nieto = Nieto()
mi_nieto.reir()
print(Nieto.mro())