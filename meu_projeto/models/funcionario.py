from models.enums1.sexo import Sexo
from models.enums1.setor import Setor

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return(f"\n Id: {self.id}"
               f"\n Nome: {self.nome}"
               f"\n Idade: {self.idade}"
               f"\n Salario: {self.salario}"
               f"\n Setor: {self.setor.value}"
               f"\n Sexo: {self.sexo.value}")