from Pedido import *
from Pedido import *
from ProcesadorDePagos import *


pedido = Pedido()
print(pedido)
pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)
print(pedido)
print(f'Precio total: {pedido.precio_total()}')
procesadorDePagos = ProcesadorDePagosConBitcoin(num_bv='ASDUX534SD35C53ASD')
procesadorDePagos.pagar(pedido,crypto='ETH')
print(pedido)
