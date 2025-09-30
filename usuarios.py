class Usuario:
    def __init__(self, nombre, edad, saldo, puntos, es_extranjero):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.puntos = puntos
        self.es_extranjero = es_extranjero

    def _calcular_nivel(self):
        pass

    def actualizar_nivel(self):
        pass

    def agregar_al_carrito(self, producto):
        pass

    def cargar_saldo(self, monto):
        pass

    def realizar_compra(self):
        pass
