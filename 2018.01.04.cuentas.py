class Cuenta:
    tipo = ""
    numero = ""
    saldo = 0.0

    def __init__(self, argTipo, argNumero, argSaldo):
        self.tipo=argTipo
        self.numero=argNumero
        self.saldo=argSaldo

    def debito (self, monto):
        self.saldo -= monto

    def credito (self, monto):
        self.saldo += monto


class Cliente:
    nombre = ""
    cedula = 0
    cuentas = []

    def __init__(self, argNombre, argCedula):
        self.nombre = argNombre
        self.cedula = argCedula

    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Transaccion:
    tipo = ""
    timestamp = ""
    monto = 0.0
    lugar = ""

    def __init__(self, argTipo, argTimestamp, argMonto, argCuenta, argCliente, argLugar):
        self.tipo = argTipo
        self.timestamp = argTimestamp
        self.monto = argMonto
        self.cuenta = argCuenta
        self.usuario = argCliente
        self.lugar = argLugar

    def retiro(self):
        self.cuenta.debito(self.monto)

    def deposito(self):
        self.cuenta.credito(self.monto)

    

cliente1 = Cliente("Alexander Olmedo", "1724885775")
cuentaC1 = Cuenta("Ahorros","12345",500.25)
cliente1.agregarCuenta(cuentaC1)

cliente2 = Cliente("Ronny Cabrera", "1236541236")
cuentaC2 = Cuenta("Corriente", "23651", 700.12)
cliente2.agregarCuenta(cuentaC2)

print cuentaC1.tipo, cuentaC1.numero, cuentaC1.saldo

t1 = Transaccion("Retiro", "01-04-2018", 456.25, cuentaC1, cliente1, "Quito")
t1.retiro()

print cuentaC1.tipo, cuentaC1.numero, cuentaC1.saldo



