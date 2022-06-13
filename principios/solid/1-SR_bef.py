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
    
    def pago(self,tipo_pago,codigo_seg):
        if tipo_pago == 'debito':
            print('Procesando pago de tipo debito')
            print(f'Verificando codigo de seguridad {codigo_seg}')
            self.estado = 'pagado'
        elif tipo_pago == 'credito':
            print('Procesando pago de tipo credito')
            print(f'Verificando codigo de seguridad {codigo_seg}')
        else: raise Exception(f'Tipo de pago desconocido: {tipo_pago}')

pedido = Pedido()
print(pedido)
pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)
print(pedido)
print(f'Precio total: {pedido.precio_total()}')
pedido.pago(tipo_pago='debito',codigo_seg=123)
print(pedido)

