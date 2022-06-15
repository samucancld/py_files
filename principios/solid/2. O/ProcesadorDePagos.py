from dataclasses import dataclass
from dataclasses import field
from typing import List
from abc import ABC, abstractmethod

class ProcesadorDePagos(ABC):
    @abstractmethod
    def pagar(self,pedido,codigo_seg):
        pass


class ProcesadorDePagosConDebito(ProcesadorDePagos):
    def pagar(self,pedido,codigo_seg):
        print('Procesando pago de tipo debito')
        print(f'Verificando codigo de seguridad {codigo_seg}')
        self.estado = 'pagado'

class ProcesadorDePagosConCredito(ProcesadorDePagos):
    def pagar(self,pedido,codigo_seg):
        print('Procesando pago de tipo credito')
        print(f'Verificando codigo de seguridad {codigo_seg}')
        self.estado = 'pagado' 

class ProcesadorDePagosConBitcoin(ProcesadorDePagos):
    def pagar(self,pedido,codigo_seg,crypto):
        print(f'Procesando pago de tipo {crypto}')
        print(f'Verificando codigo de seguridad {codigo_seg}')
        self.estado = 'pagado'