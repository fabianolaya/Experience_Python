class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio,mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros ")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.mirar()
Pajaro.poner_huevos(3)


class Personaje:
    def __init__(self, cantidad_flechas=5):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
        else:
            print("No tienes mas flechas")

Personaje.lanzar_flecha()
