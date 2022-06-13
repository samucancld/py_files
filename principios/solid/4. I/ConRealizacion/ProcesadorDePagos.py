from dataclasses import dataclass
from dataclasses import field
from typing import List
from abc import ABC, abstractmethod

class ProcesadorDePagos(ABC):
    @abstractmethod
    def pagar(self,pedido):
        pass

class ProcesadorDePagosConSMS(ProcesadorDePagos):
    @abstractmethod
    def autorizar_SMS(self,codigo_seg):
        pass

@dataclass
class ProcesadorDePagosConDebito(ProcesadorDePagosConSMS):
    codigo_seg: str
    verificado: bool = field(default=False)
    def pagar(self,pedido):
        if not self.verificado:
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
    def pagar_con_credito(self,pedido):
        print('Procesando pago de tipo credito')
        print(f'Verificando codigo de seguridad {self.codigo_seg}')
        pedido.estado = 'pagado'

@dataclass
class ProcesadorDePagosConBitcoin(ProcesadorDePagosConSMS):
    num_bv: str
    verificado: bool = field(default=False)


    def pagar(self,pedido,crypto):
        if not self.verificado:
            raise Exception('Pago no autorizado')
        print(f'Procesando pago de tipo {crypto}')
        print(f'Verificando numero de billetera virtual {self.num_bv}')
        pedido.estado = 'pagado'

    def autorizar_SMS(self,codigo_seg):
        print(f'Verificando codigo SMS: {codigo_seg}')
        self.verificado = True