from Pedido import Pedido
from ProcesadorDePagos import *
from Autorizador import *


pedido = Pedido()
print('Debug:',pedido)

pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)
print('Debug:',pedido)

print('Debug:',f'Precio total: {pedido.precio_total()}')

autorizador = AutorizadorDeCaptcha()

procesadorDePagos = ProcesadorDePagosConBitcoin(num_bv='ASDUX534SD35C53ASD',autorizador=autorizador)

print('Debug:',autorizador.esAutorizado())


autorizador.verificar_captcha()

procesadorDePagos.pagar(pedido,crypto='ETH')

print('Debug:',autorizador.esAutorizado())
print('Debug:',pedido)

