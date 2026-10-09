from enum import Enum


# Enumeraciones
class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"


class TipoAutomovil(Enum):
    CARRO_CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"


# Clase Automóvil
class Automovil:

    def __init__(
        self,
        marca,
        modelo,
        motor,
        tipo_combustible,
        tipo_automovil,
        numero_puertas,
        cantidad_asientos,
        velocidad_maxima,
        color,
        velocidad_actual=0,
    ):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual

    # Métodos Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def get_numero_puertas(self):
        return self.numero_puertas

    def get_cantidad_asientos(self):
        return self.cantidad_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    # Métodos Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        if velocidad_actual < 0:
            print("Error: No se puede asignar una velocidad negativa.")
            self.velocidad_actual = 0
        elif velocidad_actual > self.velocidad_maxima:
            print(
                "Error: La velocidad excede la máxima permitida"
                f" ({self.velocidad_maxima} km/h)."
            )
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual = velocidad_actual

    # Métodos de aceleración y movimiento
    def acelerar(self, incremento):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            print(
                "No se puede acelerar tanto. Se superaría la velocidad máxima"
                f" ({self.velocidad_maxima} km/h)."
            )
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual += incremento

    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento < 0:
            print(
                "No se puede desacelerar a una velocidad negativa. El vehículo"
                " se ha detenido."
            )
            self.velocidad_actual = 0
        else:
            self.velocidad_actual -= decremento

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print(
                "El vehículo está detenido. No se puede calcular el tiempo de"
                " llegada."
            )
            return None
        return distancia / self.velocidad_actual

    def imprimir(self):
        print("--- Datos del Automóvil ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Cantidad de asientos: {self.cantidad_asientos}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value}")
        print(f"Velocidad actual: {self.velocidad_actual} km/h")


# Función Principal
def main():
    auto = Automovil(
        marca="Toyota",
        modelo=2023,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.COMPACTO,
        numero_puertas=5,
        cantidad_asientos=5,
        velocidad_maxima=180,
        color=Color.ROJO,
    )

    auto.imprimir()
    print("\n--- Pruebas de Velocidad ---")

    auto.set_velocidad_actual(100)
    print(f"Velocidad inicial establecida: {auto.get_velocidad_actual()} km/h")

    auto.acelerar(20)
    print(f"Velocidad tras acelerar 20 km/h: {auto.get_velocidad_actual()} km/h")

    auto.desacelerar(50)
    print(
        "Velocidad tras desacelerar 50 km/h:"
        f" {auto.get_velocidad_actual()} km/h"
    )

    auto.frenar()
    print(f"Velocidad tras frenar: {auto.get_velocidad_actual()} km/h")


if __name__ == "__main__":
    main()