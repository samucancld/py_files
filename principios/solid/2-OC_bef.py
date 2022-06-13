from dataclasses import dataclass
from dataclasses import field
from typing import List

@dataclass
class Pedido:
    items: List[str] = field(init=False,default_factory=list)
    cantidades: List[int] = field(init=False,default_factory=list)
    precios: List[float] = field(init=False,default_factory=list)
    estado: str = field(default='abierto',init=False)

    def agregar_item(self, item, cantidad, precio):
        self.items.append(item)
        self.cantidades.append(cantidad)
        self.precios.append(precio)

    def precio_total(self):
        total = 0
        for i in range(len(self.precios)):
            total = total + (self.cantidades[i]*self.precios[i])
        return total

@dataclass
class ProcesadorDePagos:
    def pagar_con_debito(self,pedido,codigo_seg):
        print('Procesando pago de tipo debito')
        print(f'Verificando codigo de seguridad {codigo_seg}')
        self.estado = 'pagado'
    def pagar_con_credito(self,pedido,codigo_seg):
        print('Procesando pago de tipo credito')
        print(f'Verificando codigo de seguridad {codigo_seg}')
        self.estado = 'pagado' 


pedido = Pedido()
print(pedido)
pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)
print(pedido)
print(f'Precio total: {pedido.precio_total()}')
procesadorDePagos = ProcesadorDePagos()
procesadorDePagos.pagar_con_debito(pedido,codigo_seg=123)
print(pedido)

