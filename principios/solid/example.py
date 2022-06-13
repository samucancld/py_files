from dataclasses import dataclass, field
from typing import List

@dataclass
class Persona:
    name: str
    apellido: str
    dni: float
    mascotas: List[str] = field(init=False,default_factory=list)

    def nueva_mascota(self,mascota):
        self.mascotas.append(mascota)

@dataclass
class Pedido:
    items: List[str] = field(init=False,default_factory=list)
    cantidades: List[int] = field(init=False,default_factory=list)
    precios: List[float] = field(init=False,default_factory=list)
    estado: str = field(default='river')

    #def agregar_item(self, item, cantidad, precio):
        #self.items.append(item)
        #self.cantidades.append(cantidad)
        #self.precios.append(precio)



pedido = Pedido()
print(pedido)
#pedido.agregar_item(item='Lomito',cantidad=2,precio=600.0)



#samuca = Persona(name='Samuel',apellido='Andres',dni=42443064,mascotas=['lana'])
samuca = Persona(name='Samuel',apellido='Andres',dni=42443064)
samuca.nueva_mascota('lana')

print(samuca)