class vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice mu")

class oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "  dice bee")

class perro:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "  dice guau")

class gato:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "  dice miau")


vaca1 = vaca('Aurora')
oveja1 = oveja('Nube')
perro1 = perro('Mateo')
gato1 = gato('Isis')



def animal_habla(animal):
    animal.hablar()

animal_habla(gato1)
