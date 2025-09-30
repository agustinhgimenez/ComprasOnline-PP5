import pytest
from productos import Mueble, BebidaAlcoholica, Promocion, Pesado, TaxFree
from usuarios import Usuario
from tienda import Tienda

#1)Probar que un mueble pesado, tax-free y de promoción muestre etiqueta correcta.
#2) Probar que que un mueble pesado de $60.000 con un 30% de descuento tenga recargo por ser
#un mueble (con su recargo de $1000), recargo por envío ($3000),
#3) Probar que usuario Bronce con 1 y $5000 de saldo cuando compra una mochila sumaria 1000 puntos y quedaría con saldo en $0.
#4) Probar que el negocio aplique correctamente la penalización de morosidad.
#5) Probar que usuario Bronce con 1 punto pase a Plata al darle 5000 puntos.
#6) Probar que usuario Bronce con saldo de $4999 no puede comprar una mochila de $5000
#7) Probar que usuario menor de 18 años no puede comprar una botella de cerveza por más que le alcance su saldo.
#8) Probar que un usuario extranjero puede aprovechar el beneficio tax-free (sin IVA).
#9) Realizar un test automático que valide el siguiente escenario: usuario Bronce con 4.900
#puntos realiza una compra por $1.000. Al completar la compra gana 100 puntos, alcanzando
#exactamente los 5.000 puntos necesarios. Verificar que su nivel se actualiza automáticamente a Plata.
#10) Realizar un test automático que valide el siguiente escenario: un usuario Bronce no puede al mismo tiempo agregar mochila y cartuchera al carrito provocando una Excepción.


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


