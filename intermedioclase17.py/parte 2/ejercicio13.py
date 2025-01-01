""""Crea una excepción personalizada llamada SaldoInsuficienteError para una clase de cuenta bancaria.
"""
class SaldoInsuficienteError(Exception):
   pass

class CuentaBancaria: 
  def init(self, saldo_inicial=0): 
    self.saldo = saldo_inicial

def retirar(self, cantidad):
    if cantidad > self.saldo:
        raise SaldoInsuficienteError("Fondos insuficientes")
    self.saldo -= cantidad