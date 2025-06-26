# Funções Matemáticas no Excel

# Descrição
'''
O Excel oferece diversas funções matemáticas que facilitam cálculos como soma, média, arredondamento e obtenção de valores extremos.
Essas funções são fundamentais para análises numéricas e manipulação de dados.

Neste desafio, você receberá uma descrição textual de uma função matemática do Excel e deverá identificar corretamente o nome exato
da função correspondente.
'''
# Entrada
'''
Uma breve descrição textual de uma função matemática do Excel. As descrições podem indicar operações como soma, média, arredondamento
ou obtenção do maior ou menor valor de um intervalo. Os possíveis valores de entrada são:

    Soma os valores de um intervalo.
    Calcula a média dos valores de um intervalo.
    Arredonda um número para um número específico de casas decimais.
    Retorna o maior valor de um intervalo.
'''
# Saída
'''
Uma lista com as fórmulas exatas do Excel correspondentes às descrições fornecidas.

As funções matemáticas do Excel que podem ser retornadas são:

    =SOMA(A1:A10) → O que faz? Retorna a soma dos valores no intervalo A1:A10.
    =MÉDIA(A1:A10) → O que faz? Retorna a média aritmética dos valores no intervalo A1:A10.
    =ARRED(A1, 2) → O que faz? Arredonda o valor na célula A1 para duas casas decimais.
    =MÁXIMO(A1:A10) → O que faz? Retorna o maior valor presente no intervalo A1:A10.
'''
# Exemplos
'''
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu
programa com esses exemplos e com outros casos possíveis.
                      Entrada 	                                             Saída
Soma os valores de um intervalo 	                                     =SOMA(A1:A10)
Calcula a média dos valores de um intervalo 	                         =MÉDIA(A1:A10)
Arredonda um número para um número específico de casas decimais 	     =ARRED(A1, 2)

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''


# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma descrição e retornar a fórmula correspondente do Excel.
def identificar_funcao_matematica(descricao):
    if descricao == "Soma os valores de um intervalo.":
        return '=SOMA(A1:A10)'

    elif descricao == "Calcula a média dos valores de um intervalo.":
        return '=MÉDIA(A1:A10)'

    elif descricao == "Arredonda um número para um número específico de casas decimais.":
        return '=ARRED(A1, 2)'

    elif descricao == "Retorna o maior valor de um intervalo.":
        return '=MÁXIMO(A1:A10)'

    else:
        return "Função não encontrada"

# Imprime a fórmula correspondente à entrada fornecida
print(identificar_funcao_matematica(entrada))