from clase_habitacion import Habitacion
from clase_vivienda import Vivienda
from clase_barrio import Barrio


# Creacion de habitaciones
habitacion1 = Habitacion("Living", 80.4)
habitacion2 = Habitacion("Cocina", 35.8)
habitacion3 = Habitacion("Dormitorio", 28.5)

# Creacion de viviendas
vivienda1 = Vivienda("Calle Roca", 1, "Manzana 1", 101, 380.0)
vivienda1.obtener_habitacion(habitacion1)
vivienda1.obtener_habitacion(habitacion2)
vivienda1.obtener_habitacion(habitacion3)

vivienda2 = Vivienda("Calle Alem", 2, "Manzana 2", 102, 350.0)
vivienda2.obtener_habitacion(habitacion1)
vivienda2.obtener_habitacion(habitacion3)

# Creacion de barrio
barrio = Barrio("Barrio Union y Fuerza", "Constructora UTN")
barrio.obtenerViviendas(vivienda1)
barrio.obtenerViviendas(vivienda2)

# Mostrar los detalles del barrio/manzanas
print("Superficie total de terreno del barrio:", barrio.getSuperficieTotalTerreno())
print("Superficie total de terreno de la Manzana 1:", barrio.getSuperficieTotalTerrenoXManzana("Manzana 1"))
print("Superficie total de terreno de la Manzana 2:", barrio.getSuperficieTotalTerrenoXManzana("Manzana 2"))
print(f"Superficie total cubierta del barrio: {barrio.getSuperficieTotalCubierta()} mts de {barrio.getSuperficieTotalTerreno()} mts")