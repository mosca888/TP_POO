from clase_habitacion import Habitacion
class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []


    def obtener_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        total_metros_cuadrados = sum(habitacion.metrosCuadrados for habitacion in self.habitaciones)
        if total_metros_cuadrados > self.superficieTerreno:
            raise Exception("El total de metros cuadrados no puede ser superior a la superficie total")
        return total_metros_cuadrados
