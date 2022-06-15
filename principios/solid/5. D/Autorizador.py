from dataclasses import dataclass
from dataclasses import field
from email.mime import audio
from typing import List
from abc import ABC, abstractmethod

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

