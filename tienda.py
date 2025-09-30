from productos import BebidaAlcoholica


class Tienda:
    def __init__(self):
        self.usuarios = []
        self.productos = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def gestionar_venta(self, usuario):
        productos_a_remover = []
        for producto in usuario.carrito:
           pass #Completar 
        #dado un usuario con productos en su carrito, permite la compra. Si el
        #usuario es menor y lleva bebidas alcohólicas se las retira del carrito y las pone nuevamente en los productos disponibles.

    def gestionar_morosidad(self):
       pass #completar aplica descuento de 100 puntos a los usuarios con saldo negativo.
