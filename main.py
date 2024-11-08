from Vehiculo import *
import csv

def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, mode="w", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                datos = (vehiculo.__class__, vehiculo.__dict__)
                archivo_csv.writerow(datos)
        print("Datos guardados en vehiculos.csv")
    except Exception as e:
        print(f"Error al guardar en el archivo CSV: {e}")

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, mode="r") as archivo:
            archivo_csv = csv.reader(archivo)
            print("Lista de Vehículos:\n")
            for row in archivo_csv:
                clase, atributos = row
                print(f"{clase} : {atributos}")
    except FileNotFoundError:
        print("El archivo vehiculos.csv no existe.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")

def main():
    # Segun pdf
    particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    # Guardar los datos
    guardar_datos_csv(vehiculos)

    # mostrar los datos
    leer_datos_csv()

if __name__ == "__main__":
    main()
