import pytest
from inmuebles import Casa, PH, Departamento
from estrategia_comision import EstrategiaAlquiler, EstrategiaVenta
from operacion import Operacion
from agente import Agente
from inmobiliaria import Inmobiliaria


class MockInmueble:
    def __init__(self, valor):
        self.valor = valor

    def calcular_valor(self):
        return self.valor


class MockEstrategiaComision:
    def __init__(self, comision_fija):
        self.comision_fija = comision_fija

    def calcular_comision(self, inmueble):
        return self.comision_fija


class TestInmuebles:
    pass

class TestEstrategiaComision:
    pass

class TestOperacion:
    pass

class TestAgente:
    pass

class TestInmobiliaria:
    pass
