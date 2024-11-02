from clase_vivienda import Vivienda
class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []


    def obtenerViviendas(self, vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas if vivienda.manzana == manzana)
    
    def getSuperficieTotalCubierta(self):
        return sum(vivienda.getMetrosCuadradosCubiertos() for vivienda in self.viviendas)

