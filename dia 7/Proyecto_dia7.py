class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente :{self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}'

    def depositar(self,monto):
        if monto > 0:
            self.balance += monto
            print(f"El deposito ha sido exitoso. Nuevo balance: {self.balance}")
        else:
            print(f"El deposito no ha podido realizarse")

    def retirar(self,monto):
        if monto > self.balance:
            print("Fondos insuficientes")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor a cero")
        else:
            self.balance -= monto
            print(f"Retiro Exitoso. Nuevo balance: ${self.balance}")

def crear_cliente():

    nombre_cl = input("Ingresa tu nombre: ")
    apellido_cl = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingrese el numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl,numero_cuenta)

    return cliente

def inicio ():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elige: Depositar (D),Retirar (R),Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print('Gracias por operar en banco python')

inicio()













