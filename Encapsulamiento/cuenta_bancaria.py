class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Usando dos guiones hacemos privado al atributo
        self.__saldo = saldo_inicial

    # Setter (definir, modificar)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se ha depositado {cantidad} exitoso!")
        else:
            print("Error: no se puede depositar un saldo negativo")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado ${cantidad} exitoso!")
        else:
            print("Fondos insuficientes o cantidad inválida")

    # Getter (obtener información privada a través de un método público)
    def obtener_saldo(self):
        return f"El saldo actual de la cuenta es {self.__saldo}"