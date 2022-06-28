from dataclasses import dataclass, field

@dataclass
class Persona:
    __nombre: str
    __apellido: str
    __DNI: int = field(default=00000000)

    def getNombre(self) -> str:
        return self.__nombre

    def getDNI(self) -> int:
        return self.__DNI


#samuca = Persona('Samuel', 'Andres', 42443064)
samuca = Persona('Samuel', 'Andres', 42443064)
print(samuca.getNombre())
print(samuca.getDNI())