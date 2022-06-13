from dataclasses import dataclass
from dataclasses import field
from typing import List

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