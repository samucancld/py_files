from dataclasses import dataclass
from dataclasses import field
from email.mime import audio
from typing import List
from abc import ABC, abstractmethod
from Autorizador import *

class ProcesadorDePagos(ABC):
    @abstractmethod
    def pagar(self,pedido):
        pass

@dataclass
class ProcesadorDePagosConDebito(ProcesadorDePagos):
    codigo_seg: str
    autorizador: Autorizador
    def pagar(self,pedido):
        if not self.autorizador.esAutorizado():
            raise Exception('Pago no autorizado')
        print('Procesando pago de tipo debito')
        print(f'Verificando codigo de seguridad {self.codigo_seg}')
        pedido.estado = 'pagado'
    
    def autorizar_SMS(self,codigo_seg):
        print(f'Verificando codigo SMS: {codigo_seg}')
        self.verificado = True

@dataclass
class ProcesadorDePagosConCredito(ProcesadorDePagos):
    codigo_seg: str
    def pagar(self,pedido):
        print('Procesando pago de tipo credito')
        print(f'Verificando codigo de seguridad {self.codigo_seg}')
        pedido.estado = 'pagado'

@dataclass
class ProcesadorDePagosConBitcoin(ProcesadorDePagos):
    num_bv: str
    autorizador: Autorizador
    def pagar(self,pedido,crypto):
        if not self.autorizador.esAutorizado():
            raise Exception('Pago no autorizado')
        print(f'Procesando pago de tipo {crypto}')
        print(f'Verificando numero de billetera virtual {self.num_bv}')
        pedido.estado = 'pagado'