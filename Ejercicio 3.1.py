from enum import Enum


# 1. Enumeración
class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"


# 2. Clase Planeta
class Planeta:
    UA_EN_KM = 149597870

    def __init__(
        self,
        nombre=None,
        cantidad_satelites=0,
        masa=0.0,
        volumen=0.0,
        diametro=0,
        distancia_media_sol=0,
        tipo_planeta=None,
        es_observable=False,
    ):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_media_sol = distancia_media_sol
        self.tipo_planeta = tipo_planeta
        self.es_observable = es_observable

    def imprimir(self):
        print(f"--- Información del Planeta: {self.nombre} ---")
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(
            f"Distancia media al Sol: {self.distancia_media_sol} millones"
            " de km"
        )
        print(
            "Tipo de planeta:"
            f" {self.tipo_planeta.value if self.tipo_planeta else 'No asignado'}"
        )
        print(
            "Observable a simple vista:"
            f" {'Sí' if self.es_observable else 'No'}"
        )

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0.0
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        distancia_km = self.distancia_media_sol * 1_000_000
        distancia_ua = distancia_km / self.UA_EN_KM
        return distancia_ua > 3.4


# 3. Función Principal
def main():
    tierra = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.9736e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_media_sol=150,
        tipo_planeta=TipoPlaneta.TERRESTRE,
        es_observable=True,
    )

    jupiter = Planeta(
        nombre="Júpiter",
        cantidad_satelites=95,
        masa=1.8986e27,
        volumen=1.43128e15,
        diametro=139822,
        distancia_media_sol=778,
        tipo_planeta=TipoPlaneta.GASEOSO,
        es_observable=True,
    )

    tierra.imprimir()
    print(f"Densidad: {tierra.calcular_densidad():.4e} kg/km³")
    print(
        f"¿Es planeta exterior?: {'Sí' if tierra.es_planeta_exterior() else 'No'}"
    )
    print()

    jupiter.imprimir()
    print(f"Densidad: {jupiter.calcular_densidad():.4e} kg/km³")
    print(
        f"¿Es planeta exterior?: {'Sí' if jupiter.es_planeta_exterior() else 'No'}"
    )


if __name__ == "__main__":
    main()