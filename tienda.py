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

    def gestionar_morosidad(self):
       pass #completar