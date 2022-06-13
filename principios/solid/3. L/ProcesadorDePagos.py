from dataclasses import dataclass
from dataclasses import field
from typing import List
from abc import ABC, abstractmethod

class ProcesadorDePagos(ABC):
    @abstractmethod
    def pagar(self,pedido):
        pass
#se quit el atributo codigo de seguridad ya que deja de tener
#sentido para todas las clases que implementan la interfaz
@dataclass
class ProcesadorDePagosConDebito(ProcesadorDePagos):
    codigo_seg: str
    def pagar(self,pedido):
        print('Procesando pago de tipo debito')
        print(f'Verificando codigo de seguridad {self.codigo_seg}')
        pedido.estado = 'pagado'
@dataclass
class ProcesadorDePagosConCredito(ProcesadorDePagos):
    codigo_seg: str
    def pagar_con_credito(self,pedido):
        print('Procesando pago de tipo credito')
        print(f'Verificando codigo de seguridad {self.codigo_seg}')
        pedido.estado = 'pagado' 
@dataclass
class ProcesadorDePagosConBitcoin(ProcesadorDePagos):
    num_bv: str
    def pagar(self,pedido,crypto):
        print(f'Procesando pago de tipo {crypto}')
        print(f'Verificando numero de billetera virtual {self.num_bv}')
        pedido.estado = 'pagado'