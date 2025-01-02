""""Crear una clase CuentaBancaria con métodos para depositar, retirar y consultar el saldo.
"""

class CuentaBancaria:
    def __init__(self, usuario, saldo):
        self.usuario = usuario
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito

    def retirar(self, retiro):
        if self.saldo > retiro:
            self.saldo -= retiro
        else:
            "Fondos insuficientes"
    
    def consultar(self):
        return self.saldo
    
cuenta1 =CuentaBancaria("Eduardo Molina", 5000)

print(cuenta1.consultar())
cuenta1.depositar(20)
print(cuenta1.consultar())
cuenta1.retirar(40)
print(cuenta1.consultar())

