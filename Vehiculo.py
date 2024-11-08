class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, "
                f"{self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc")

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return super().__str__() + f" Puestos: {self.nro_puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f" Carga: {self.carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return (super().__str__() + f" Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}")

# Parte1
def main():
    vehiculos = []
    cantidad = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(cantidad):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = input("Inserte el número de ruedas: ")
        velocidad = input("Inserte la velocidad en km/h: ")
        cilindrada = input("Inserte el cilindraje en cc: ")
        vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)

    # Print
    print("\nImprimiendo por pantalla los Vehículos:\n")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(f"Datos del vehículo {i} : {vehiculo}")

if __name__ == "__main__":
    main()
