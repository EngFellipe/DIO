# Descrição
""" Implemente um sistema que gerencie várias contas bancárias. Cada conta será representada como uma instância da classe 
ContaBancaria criada no desafio anterior. O sistema deve permitir que você crie contas para diferentes titulares e liste 
todas as contas cadastradas ao final da execução. """

# Requisitos
""" O sistema deve permitir:
    - Criar contas:  Ao criar uma conta, forneça o nome do titular e o saldo inicial no formato "Titular, SaldoInicial".
    - Listar contas:  Ao digitar o comando especial "FIM", o sistema deverá listar todas as contas cadastradas no formato especificado.
"""

# Entrada
""" O sistema deve permitir:
    - Criação de contas no formato: "Titular, SaldoInicial".
    - Um comando especial "FIM" será usado para encerrar o processo de entrada e listar as contas.
"""

# Saída
""" Liste todas as contas cadastradas no formato: "Titular: X, Saldo: R$ Y" """

# Exemplos
"""
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada 	                          Saída
João, 500
Maria, 1000
FIM 	                   João: R$ 500, Maria: R$ 1000

Ana, 150
Bruno, 250
FIM 	                    Ana: R$ 150, Bruno: R$ 250

Fernando, 50
Gustavo, 75
Helena, 125
FIM 	          Fernando: R$ 50, Gustavo: R$ 75, Helena: R$ 125

"""


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

#TODO: Implemente a classe SistemaBancario:
class SistemaBancario:

    # TODO: Inicialize a lista de contas:
    def __init__(self):
        self.contas = []

    # TODO: Crie uma nova conta e adicione à lista de contas:
    def criar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        self.contas.append(conta)

    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    def listar_contas(self):
        saida = ", ".join(f"{conta.titular}: R$ {conta.saldo}" for conta in self.contas)
        print(saida)

#TODO: Crie uma instância de SistemaBancario:
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()