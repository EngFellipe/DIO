# Contando Valores no Excel

# Descrição
'''
O Excel oferece diversas funções para contar células em um intervalo, dependendo do tipo de dado ou critério desejado. 
Neste desafio, você receberá uma descrição de uma função específica de contagem do Excel e deverá identificar corretamente 
o nome da função correspondente.
'''
# Entrada
'''
Uma breve descrição textual de uma função de contagem utilizada no Excel. A descrição pode indicar o tipo de célula que deve 
ser contada (por exemplo, números, células não vazias, células vazias) ou se há critérios específicos para a contagem.

    Conta células que atendem a um critério ou contêm números.
    Conta o número de células que não estão vazias em um intervalo.
    Conta células que atendem a um critério específico.
    Conta células que atendem a vários critérios em múltiplos intervalos.
'''

# Saída
'''
Uma lista com os nomes exatos das funções do Excel correspondentes às descrições fornecidas.

As funções de contagem do Excel que podem ser retornadas são:

    =CONT.NÚM(A1:A10) →  O que faz? Conta células que atendem a um critério ou contêm números.
    =CONT.VALORES(A1:A10) →  O que faz? Conta o número de células que não estão vazias em um intervalo.
    =CONT.SE(A1:A10, ">10") →   O que faz? Conta células que atendem a um critério específico. 
    =CONT.SES(A1:A10, ">10", B1:B10, "<50") → O que faz? Conta células que atendem a vários critérios em múltiplos intervalos. 
'''
# Exemplos
'''
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar 
seu programa com esses exemplos e com outros casos possíveis.
                    Entrada 	                                                        Saída
Conta células que atendem a um critério ou contêm números. 	                      =CONT.NÚM(A1:A10)
Conta o número de células que não estão vazias em um intervalo. 	            =CONT.VALORES(A1:A10)
Conta células que atendem a um critério específico. 	                       =CONT.SE(A1:A10, ">10")

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma descrição e retornar o nome da função do Excel correspondente.
def identificar_funcao_contagem(descricao):
    if descricao == "Conta células que atendem a um critério ou contêm números.":
        return '=CONT.NÚM(A1:A10)'

    elif descricao == "Conta o número de células que não estão vazias em um intervalo.":
        return '=CONT.VALORES(A1:A10)'

    elif descricao == "Conta células que atendem a um critério específico.":
        return '=CONT.SE(A1:A10, ">10")'

    elif descricao == "Conta células que atendem a vários critérios em múltiplos intervalos.":
        return '=CONT.SES(A1:A10, ">10", B1:B10, "<50")'

    else:
        return "Função não encontrada"

# Imprime o nome da função correspondente à entrada fornecida
print(identificar_funcao_contagem(entrada))