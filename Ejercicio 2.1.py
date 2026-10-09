class Persona:
    def __init__(self, nombre, apellido, numero_documento_identidad, ano_nacimiento):
        # Atributos de una persona
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento_identidad = numero_documento_identidad
        self.ano_nacimiento = ano_nacimiento


    # Método para imprimir los datos de una persona
    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellido = {self.apellido}")
        print(f"Número de documento de identidad = {self.numero_documento_identidad}")
        print(f"Año de nacimiento = {self.ano_nacimiento}")

        print()


p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
p2 = Persona("Diana", "Soto", "1053223344", 2001)

p1.imprimir()
p2.imprimir()

