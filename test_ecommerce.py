import pytest
from productos import Mueble, BebidaAlcoholica, Promocion, Pesado, TaxFree
from usuarios import Usuario
from tienda import Tienda


class MockProducto:
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base
        self.modificadores = []

    def agregar_modificador(self, modificador):
        self.modificadores.append(modificador)

    def calcular_precio_venta(self, usuario):
        precio = self.precio_base
        for modificador in self.modificadores:
            precio = modificador.aplicar_modificador(precio, usuario)
        return precio

    def puede_ser_comprado_por(self, usuario):
        return True


