from entidad_ingrediente import Ingrediente
from entidad_plato import Plato

class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []

    def cargar_plato(self):
        nombre = input("Ingrese el nombre del plato: ")
        precio = float(input("Ingrese el precio del plato: "))
        bebida = input("¿Es una bebida? (si/no): ")

        plato = Plato(nombre, precio, bebida)

        if bebida == "no":
            while True:
                nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")
                cantidad = float(input("Ingrese la cantidad del ingrediente: "))
                unidad_medida = input("Ingrese la unidad de medida del ingrediente: ")
                ingrediente = Ingrediente(nombre_ingrediente, cantidad, unidad_medida)
                plato.agregar_ingrediente(ingrediente)

                continuar = input("¿Desea agregar otro ingrediente? (si/no): ")
                if continuar == 'no':
                    break

        self.platos_menu.append(plato)

    def mostrar_menu(self):
        print("-----------MENÚ----------------")
        for plato in self.platos_menu:
            plato.mostrar_plato()
