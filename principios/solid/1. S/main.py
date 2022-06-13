from Pedido import Pedido
from ProcesadorDePagos import ProcesadorDePagos

pedido = Pedido()
print(pedido)
pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)
print(pedido)
print(f'Precio total: {pedido.precio_total()}')
procesadorDePagos = ProcesadorDePagos()
procesadorDePagos.pagar_con_debito(pedido,codigo_seg=123)
print(pedido)
