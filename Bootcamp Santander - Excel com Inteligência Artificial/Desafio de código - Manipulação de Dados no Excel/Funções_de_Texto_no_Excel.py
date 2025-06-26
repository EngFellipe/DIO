# Funções de Texto no Excel

# Descrição
'''
O Excel possui diversas funções para manipulação de texto, como extração de caracteres, alteração de letras maiúsculas e minúsculas
e substituição de partes do texto. Neste desafio, você deve identificar a função correta com base em sua descrição.
'''
# Entrada
'''
Uma breve descrição textual de uma função de manipulação de texto no Excel. As descrições podem indicar ações como conversão para
maiúsculas ou minúsculas, extração de caracteres ou substituição de palavras. Os possíveis valores de entrada são:

    Converte o texto para maiúsculas.
    Converte o texto para minúsculas.
    Substitui parte de um texto por outro.
    Extrai um número específico de caracteres do início do texto.
'''
# Saída
'''
O nome exato da função do Excel correspondente à descrição fornecida. As possíveis saídas são:

    =MAIÚSCULA(A1) →  O que faz? Converte o texto da célula A1 para maiúsculas.
    =MINÚSCULA(A1) →  O que faz? Converte o texto da célula A1 para minúsculas.
    =SUBSTITUIR(A1, "velho", "novo") →  O que faz? Substitui a palavra "velho" por "novo" no conteúdo da célula A1. 
    =ESQUERDA(A1, 5) →  O que faz? Extrai os 5 primeiros caracteres do texto contido na célula A1. 
'''
# Exemplos
'''
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu
programa com esses exemplos e com outros casos possíveis.
           Entrada 	                                          Saída
Converte o texto para maiúsculas. 	                      =MAIÚSCULA(A1)
Converte o texto para minúsculas. 	                      =MINÚSCULA(A1)
Substitui parte de um texto por outro. 	          =SUBSTITUIR(A1, "velho", "novo")

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma descrição e retornar o nome da função do Excel correspondente.
def identificar_funcao_texto(descricao):
    if descricao == "Converte o texto para maiúsculas.":
        return '=MAIÚSCULA(A1)'

    elif descricao == "Converte o texto para minúsculas.":
        return '=MINÚSCULA(A1)'

    elif descricao == "Substitui parte de um texto por outro.":
        return '=SUBSTITUIR(A1, "velho", "novo")'

    elif descricao == "Extrai um número específico de caracteres do início do texto.":
        return '=ESQUERDA(A1, 5)'

    else:
        return "Função não encontrada"

# Imprime o nome da função correspondente à entrada fornecida
print(identificar_funcao_texto(entrada))