class Usuario:
    def __init__(self, nombre, edad, saldo, puntos, es_extranjero):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.puntos = puntos
        self.es_extranjero = es_extranjero
        self.carrito = []
        self.nivel = self._calcular_nivel()

    def _calcular_nivel(self):
       pass

    def actualizar_nivel(self):
        self.nivel = self._calcular_nivel()

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)

    def cargar_saldo(self, monto):
        self.saldo += monto

    def realizar_compra(self):
        total = 0
        for producto in self.carrito:
            total += producto.calcular_precio_venta(self)
        pass
        self.saldo -= total
        puntos_ganados = total * 0.1
        self.puntos += puntos_ganados
        self.actualizar_nivel()
        self.carrito = []
        return puntos_ganados