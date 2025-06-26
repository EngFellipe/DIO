# Funções de Data e Hora no Excel

# Descrição
'''
O Excel oferece funções para trabalhar com datas e horas, permitindo calcular intervalos, extrair partes específicas de uma data e
obter valores de tempo formatados. Essas funções são essenciais para manipulação e análise de dados temporais.

Neste desafio, você receberá uma descrição textual de uma função de data ou hora do Excel e deverá identificar corretamente a fórmula
exata correspondente.
'''
# Entrada
'''
Uma breve descrição textual de uma função de manipulação de data e hora no Excel. As descrições podem indicar ações como extração do
dia, mês ou ano de uma data, além da obtenção da data e hora atual. Os possíveis valores de entrada são:

    Retorna o dia do mês de uma data.
    Retorna o mês de uma data.
    Retorna o ano de uma data.
    Retorna a data e hora atuais.
'''
# Saída
'''
Uma lista com as fórmulas exatas do Excel correspondentes às descrições fornecidas.

As funções de data e hora do Excel que podem ser retornadas são:

    =DIA(A1) → O que faz? Extrai o dia do mês da data contida na célula A1.
    =MÊS(A1) → O que faz? Extrai o mês da data contida na célula A1.
    =ANO(A1) → O que faz? Extrai o ano da data contida na célula A1.
    =AGORA() → O que faz? Retorna a data e hora atuais do sistema.
'''
# Exemplos
'''
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu
programa com esses exemplos e com outros casos possíveis.
            Entrada 	                       Saída
Retorna o dia do mês de uma data. 	          =DIA(A1)
Retorna o mês de uma data. 	                  =MÊS(A1)
Retorna o ano de uma data. 	                  =ANO(A1)

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''


# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma descrição e retornar a fórmula correspondente do Excel.
def identificar_funcao_data(descricao):
    if descricao == "Retorna o dia do mês de uma data.":
        return '=DIA(A1)'

    elif descricao == "Retorna o mês de uma data.":
        return '=MÊS(A1)'

    elif descricao == "Retorna o ano de uma data.":
        return '=ANO(A1)'

    elif descricao == "Retorna a data e hora atuais.":
        return '=AGORA()'

    else:
        return "Função não encontrada"

# Imprime a fórmula correspondente à entrada fornecida
print(identificar_funcao_data(entrada))