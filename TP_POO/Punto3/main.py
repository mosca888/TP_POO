from entidad_menurestaurant import MenuRestaurant
from entidad_ingrediente import Ingrediente
from entidad_plato import Plato

menu = MenuRestaurant()
while True:
    menu.cargar_plato()
    continuar = input("¿Desea agregar otro plato? (si/no): ")
    if continuar == 'no':
        break

menu.mostrar_menu()

