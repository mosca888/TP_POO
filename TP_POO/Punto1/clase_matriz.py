from clase_celda import Celda

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, celda):
        for i in self.celdasMatriz:
            if i.fila == celda.fila and i.columna == celda.columna:
                print("La celda ya existe en la matriz!")
                return
        self.celdasMatriz.append(celda)

    def obtener_valor(self, fila, columna):
        for i in self.celdasMatriz:
            if i.fila == fila and i.columna == columna:
                return i.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

    def mostrar_celdas(self):
        for i in self.celdasMatriz:
            print(f"[{i.fila}][{i.columna}] = {i.valor}")
