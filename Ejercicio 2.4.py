import math


# Clase Círculo
class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio**2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Clase Rectángulo
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# Clase Cuadrado
class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

    def calcular_perimetro(self):
        return 4 * self.lado


# Clase Triángulo Rectángulo
class TrianguloRectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif (
            self.base == self.altura
            or self.base == hipotenusa
            or self.altura == hipotenusa
        ):
            return "Isósceles"
        else:
            return "Escaleno"


# Clase de Prueba / Función Principal
def main():
    circulo = Circulo(2)
    rectangulo = Rectangulo(1, 2)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 4)

    print("--- CÍRCULO ---")
    print(f"Área: {circulo.calcular_area():.2f} cm2")
    print(f"Perímetro: {circulo.calcular_perimetro():.2f} cm\n")

    print("--- RECTÁNGULO ---")
    print(f"Área: {rectangulo.calcular_area():.2f} cm2")
    print(f"Perímetro: {rectangulo.calcular_perimetro():.2f} cm\n")

    print("--- CUADRADO ---")
    print(f"Área: {cuadrado.calcular_area():.2f} cm2")
    print(f"Perímetro: {cuadrado.calcular_perimetro():.2f} cm\n")

    print("--- TRIÁNGULO RECTÁNGULO ---")
    print(f"Área: {triangulo.calcular_area():.2f} cm2")
    print(f"Perímetro: {triangulo.calcular_perimetro():.2f} cm")
    print(f"Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm")
    print(f"Tipo de triángulo: {triangulo.determinar_tipo_triangulo()}")


if __name__ == "__main__":
    main()