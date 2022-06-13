from dataclasses import dataclass, field
from typing import List
from abc import ABC, abstractmethod

@dataclass
class Persona:
    nombre: str = field(init=False,default='')
    apellido: str = field(init=False,default='')
    nombre_y_apellido: str = field(init=False)

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido


    def __init__(self) -> None:
        pass

    def __post_init__(self) -> None:
        self.nombre_y_apellido = f'{self.nombre} {self.apellido}'
    

persona = Persona()
persona.setApellido('Andres')
persona.setNombre('Samuel')
persona.__post_init__()
print(persona)