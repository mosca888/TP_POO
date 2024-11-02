from clase_matriz import Matriz
from clase_celda import Celda

matriz = Matriz()

while True:
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    valor = input("Ingrese el valor para la celda (o 'FIN' para terminar): ")

    if valor == "FIN":
        break

    nueva_celda = Celda(fila, columna, valor)
    matriz.agregar_celda(nueva_celda)

print("\nValores cargados en la matriz:")
matriz.mostrar_celdas()


fila = int(input("\nIngrese la fila para buscar el valor: "))
columna = int(input("Ingrese la columna para buscar el valor: "))
print(matriz.obtener_valor(fila, columna))