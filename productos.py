from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    def agregar_modificador(self, modificador):
        pass

    def calcular_precio_venta(self, usuario):
        pass

    def puede_ser_comprado_por(self, usuario):
        pass

class Mueble(Producto):
    def calcular_precio_venta(self, usuario):
        pass

class Indumentaria(Producto):
    pass

class BebidaAlcoholica(Producto):
    def puede_ser_comprado_por(self, usuario):
        pass

class ModificadorEstrategia(ABC):
    def aplicar_modificacion(self, precio, usuario):
        pass

class Promocion(ModificadorEstrategia):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar_modificacion(self, precio, usuario):
        pass

class Pesado(ModificadorEstrategia):
    def aplicar_modificacion(self, precio, usuario):
        pass

class TaxFree(ModificadorEstrategia):
    def aplicar_modificacion(self, precio, usuario):
        pass
