class Plato:
    def __init__(self, nombre_completo, precio, bebida):
        self.nombre_completo = nombre_completo
        self.precio = precio
        self.es_bebida = bebida
        self.ingredientes = [] if not bebida else None

    def agregar_ingrediente(self, ingrediente):
        if not self.es_bebida:
            self.ingredientes.append(ingrediente)

    def mostrar_plato(self):
        print(f"{self.nombre_completo}")
        print(f"Precio: $ {self.precio}")
        if self.ingredientes:
            print("Ingredientes:")
            for ingrediente in self.ingredientes:
                print(ingrediente)
        print("----------------------------------")
