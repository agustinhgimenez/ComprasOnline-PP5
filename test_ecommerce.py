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

class MockUsuario:
    def __init__(self, nombre, edad, saldo, puntos, es_extranjero):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.puntos = puntos
        self.es_extranjero = es_extranjero
        self.carrito = []
        self.nivel = self.calcular_nivel()

    def calcular_nivel(self):
       pass

    def actualizar_nivel(self):
        self.nivel = self.calcular_nivel()

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)

    def cargar_saldo(self, monto):
        self.saldo += monto

    def realizar_compra(self):
        total = 0
        for producto in self.carrito:
            total += producto.calcular_precio_venta(self)
            #completar
        pass 
        self.saldo -= total # debitar el monto de su saldo;
        puntos_ganados = total * 0.1 
        self.puntos += puntos_ganados # acreditar puntos equivalentes al 10% del valor pagado;
        self.actualizar_nivel()  # Luego de cada compra se actualiza el nivel del usuario.
        self.carrito = [] #vaciar el carrito.
        return puntos_ganados
    
    def aplicar_morosidad(self):
        if self.saldo < 0:
            self.puntos -= 100
            self.actualizar_nivel()


#1)Probar que un mueble pesado, tax-free y de promoción muestre etiqueta correcta.
def test_mueble_pesado_taxfree_promocion_etiqueta():
    pass

#2) Probar que que un mueble pesado de $60.000 con un 30% de descuento tenga recargo por ser
#un mueble (con su recargo de $1000), recargo por envío ($3000),
def test_mueble_pesado_precio():
    usuario2 = MockUsuario("Agustin",27,100000,0,False) # Agustin , 27 años , saldo 100 mil , puntos 0 , no es extranjero
    producto2 = Mueble("Silla",60000) 
    producto2.agregar_modificador(Pesado())
    producto2.agregar_modificador(Promocion(30))
    precio = producto2.calcular_precio_venta(usuario2)
    assert precio == pytest.approx(60000* 0.7 + 1000 + 3000)

#3) Probar que usuario Bronce con 1 y $5000 de saldo cuando compra una mochila sumaria 1000 puntos y quedaría con saldo en $0.
def test_usuario_bronce_compra_mochila():
    usuario3 = MockUsuario("Carlos", 20, 5000, 0, False)
    producto3 = MockProducto("Mochila", 5000)
    usuario3.agregar_al_carrito(producto3)
    usuario3.realizar_compra()
    assert usuario3.puntos == 500
    assert usuario3.saldo == 0

#4) Probar que el negocio aplique correctamente la penalización de morosidad.
def test_aplicar_morosidad():
    usuario4 = MockUsuario("Luis", 25, -100, 6000, False)
    usuario4.aplicar_morosidad()
    assert usuario4.puntos == 5900

#5) Probar que usuario Bronce con 1 punto pase a Plata al darle 5000 puntos.
def test_usuario_bronce_a_plata():
    usuario5 = MockUsuario("Maria", 22, 10000, 4900, False)
    producto5 = MockProducto("Libro", 1000)
    usuario5.agregar_al_carrito(producto5)
    usuario5.realizar_compra()
    #falta assert

#6) Probar que usuario Bronce con saldo de $4999 no puede comprar una mochila de $5000
def test_usuario_bronce_saldo_insuficiente():
    usuario6 = MockUsuario("Pedro", 20, 4999, 0, False)
    producto6 = MockProducto("Mochila", 5000)
    usuario6.agregar_al_carrito(producto6)
    with pytest.raises(Exception):
        usuario6.realizar_compra()

#7) Probar que usuario menor de 18 años no puede comprar una botella de cerveza por más que le alcance su saldo.
def test_usuario_menor_no_compra_bebida():
    usuario7=MockUsuario("Nino", 17, 10000, 0, False)
    producto7 = BebidaAlcoholica("Cerveza", 200)
    usuario7.agregar_al_carrito(producto7)

#8) Probar que un usuario extranjero puede aprovechar el beneficio tax-free (sin IVA).
def test_usuario_extranjero_taxfree():
    usuario8 = MockUsuario("John", 30, 10000, 0, True)
    producto8 = MockProducto("Camisa", 1000)
    producto8.agregar_modificador(TaxFree())
    precio = producto8.calcular_precio_venta(usuario8)
    assert precio == 1000

#9) Realizar un test automático que valide el siguiente escenario: usuario Bronce con 4.900
#exactamente los 5.000 puntos necesarios. Verificar que su nivel se actualiza automáticamente a Plata.
def test_usuario_bronce_actualizacion_plata():
    usuario9 = MockUsuario("Sofia", 25, 1000, 4900, False)
    producto9 = MockProducto("Lapiz", 1000)
    usuario9.agregar_al_carrito(producto9)
    usuario9.realizar_compra()
    #falta completar assert

#10) Realizar un test automático que valide el siguiente escenario: un usuario Bronce no puede al mismo tiempo agregar mochila y cartuchera al carrito provocando una Excepción.
def test_usuario_bronce_no_multiples_productos():
    usuario10 = MockUsuario("Tomas", 20, 10000, 0, False)
    producto10 = MockProducto("Mochila", 5000)
    cartuchera10_2 = MockProducto("Cartuchera", 1000)
    usuario10.agregar_al_carrito(producto10)
    with pytest.raises(Exception):
        usuario10.agregar_al_carrito(cartuchera10_2)