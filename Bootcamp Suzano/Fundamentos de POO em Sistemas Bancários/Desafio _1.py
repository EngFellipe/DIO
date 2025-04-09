# Descrição
""" Implemente uma classe chamada ContaBancaria para representar uma conta bancária simples. Essa classe deve permitir 
que você realize as operações básicas de uma conta: depósito, saque e consulta de saldo. O saldo negativo.
"""

# Requisitos
"""
A classe ContaBancaria deve ter:
    Atributos:
        - titular (nome do dono da conta).
        - saldo (saldo inicial, que começa com 0 por padrão).
    Métodos:
        - depositar(valor): adiciona o valor informado ao saldo.
        - sacar(valor): subtrai o valor informado do saldo, se houver saldo suficiente. Caso contrário, exiba a mensagem "Saque não permitido".
        - saldo_atual(): retorna o saldo atual da conta.

"""

# Entrada
"""
1.  Nome do titular (string).
2.  Sequência de valores representando operações de depósito e saque:
    - Valores positivos representam depósitos.
    - Valores negativos representam saques.

"""

# Saída
""" Exiba as operações realizadas e o saldo final no formato: "Operações: +500, -200; Saldo: 300" """

# Exemplos
"""
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada 	                                         Saída
Maria
100, -50, 200, -300 	    Operações: +100, -50, +200, Saque não permitido; Saldo: 250

Carlos
1000, -500, -600 	        Operações: +1000, -500, Saque não permitido; Saldo: 500

Ana
0, 100
	                         Operações: 0, +100; Saldo: 100
"""


class ContaBancaria:
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    # TODO: Implemente o método para realizar um saque:
    
        # TODO: Verifique se há saldo suficiente para o saque
         
            # TODO: Subtraia o valor do saldo (valor já é negativo)
            
            # TODO: Registre a operação e retorne a  mensagem de saque negado
    def sacar(self, valor):
        # valor é negativo, por isso usamos abs(valor)
        if self.saldo + valor >= 0:  # valor é negativo, então somar equivale a subtrair
            self.saldo += valor
            self.operacoes.append(str(valor))
        else:
            self.operacoes.append("Saque não permitido")

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    def extrato(self):
        operacoes_formatadas = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_formatadas}; Saldo: {self.saldo}")


nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()