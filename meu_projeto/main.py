import os
from models.funcionario import Funcionario
from models.enums1.sexo import Sexo
from models.enums1.setor import Setor

os.system("cls || clear")

funcionario1 = Funcionario(2133, "Ruan", 22, 5700, Setor.FINANCEIRO, Sexo.MASCULINO)

print(funcionario1)