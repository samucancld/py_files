from Pedido import Pedido
from ProcesadorDePagos import *

pedido = Pedido()
print(pedido)
pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)
print(pedido)
print(f'Precio total: {pedido.precio_total()}')
procesadorDePagos = ProcesadorDePagosConBitcoin()
procesadorDePagos.pagar(pedido,codigo_seg=123,crypto='ETH')
print(pedido)
