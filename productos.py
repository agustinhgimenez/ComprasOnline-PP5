from abc import ABC, abstractmethod

#Clase Producto
class Producto(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base
        self.modificadores = [] #Un producto puede tener multiples modificadores

    def agregar_modificador(self, modificador):
        self.modificadores.append(modificador)

    def calcular_precio_venta(self, usuario):
        precio = self.precio_base
        for modificador in self.modificadores:
            precio = modificador.aplicar_modificador(precio, usuario)
        return precio

    def puede_ser_comprado_por(self, usuario):
        return True

#Clase Mueble
class Mueble(Producto):
    def calcular_precio_venta(self, usuario):
        precio = super().calcular_precio_venta(usuario)
        return precio + 1000

#Clase Indumentaria
class Indumentaria(Producto):
    pass

#Clase Bebida Alcoholica
class BebidaAlcoholica(Producto):
    def puede_ser_comprado_por(self, usuario):
        return usuario.edad >= 18

#Patron Strategy - Modificador - Clase Abstracta
class ModificadorEstrategia(ABC):
    @abstractmethod
    def aplicar_modificador(self, precio, usuario):
        pass


class Promocion(ModificadorEstrategia):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje
   
    def aplicar_modificador(self, precio, usuario):
        return precio * (1 - self.porcentaje / 100) #Reduce el precio de venta en un porcentaje determinado


class Pesado(ModificadorEstrategia):
    def aplicar_modificador(self, precio, usuario):
        return precio + 3000   # Agrega un extra de 3000


class TaxFree(ModificadorEstrategia):
    def aplicar_modificador(self, precio, usuario):
        if usuario.es_extranjero:
            return precio  #usuario extranjero sin taxes
        else:
            return precio * 1.21  #usuario nacion , con IVA 21%