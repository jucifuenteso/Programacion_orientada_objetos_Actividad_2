from enum import Enum


# Enumeración para el tipo de cuenta
class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"


# Clase CuentaBancaria
class CuentaBancaria:

    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        print("--- Datos de la Cuenta Bancaria ---")
        print(f"Titular: {self.nombres} {self.apellidos}")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta.value}")
        print(f"Saldo actual: ${self.saldo:,.2f}")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(
                f"Consignación exitosa de ${valor:,.2f}. Nuevo saldo:"
                f" ${self.saldo:,.2f}"
            )
        else:
            print("El valor a consignar debe ser mayor a cero.")

    def retirar(self, valor):
        if valor <= 0:
            print("El valor a retirar debe ser mayor a cero.")
        elif valor > self.saldo:
            print(
                f"No se puede retirar ${valor:,.2f}. Saldo insuficiente"
                f" (${self.saldo:,.2f})."
            )
        else:
            self.saldo -= valor
            print(
                f"Retiro exitoso de ${valor:,.2f}. Nuevo saldo:"
                f" ${self.saldo:,.2f}"
            )


# Función Principal
def main():
    cuenta = CuentaBancaria(
        nombres="Juan",
        apellidos="Pérez",
        numero_cuenta=123456789,
        tipo_cuenta=TipoCuenta.AHORROS,
    )

    cuenta.imprimir()
    print()

    print(f"Consultar saldo inicial: ${cuenta.consultar_saldo():,.2f}")

    # Probar consignación
    cuenta.consignar(500000)

    # Probar retiro exitoso
    cuenta.retirar(200000)

    # Probar retiro que supera el saldo disponible
    cuenta.retirar(400000)

    print()
    cuenta.imprimir()


if __name__ == "__main__":
    main()