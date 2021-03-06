from dataclasses import dataclass
from dataclasses import field
from email.mime import audio
from typing import List
from abc import ABC, abstractmethod

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

class ProcesadorDePagos(ABC):
    @abstractmethod
    def pagar(self,pedido):
        pass

@dataclass
class Autorizador(ABC):
    @abstractmethod
    def esAutorizado(self) -> bool:
        pass


@dataclass
class AutorizadorDePagosSMS(Autorizador):
    autorizado: bool = field(default=False)

    def verificar_codigo(self,codigo):
        print(f'Verificando codigo SMS {codigo}')
        self.autorizado = True

    def esAutorizado(self) -> bool:
        return self.autorizado

@dataclass
class AutorizadorDeCaptcha(Autorizador):
    autorizado: bool = field(default=False)

    def verificar_captcha(self):
        print(f'Verificando captcha')
        self.autorizado = True

    def esAutorizado(self) -> bool:
        return self.autorizado



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
    def pagar_con_credito(self,pedido):
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

