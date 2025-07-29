"""
    4- Calculadora de Idade em Dias
    Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

    * Solicite o ano de nascimento da pessoa.  
    * Considere o ano atual automaticamente.  
    * Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
    * Exiba o resultado final.
"""

from datetime import date

def calcula_idade_dias(ano_nascimento):
    ano_atual = date.today().year
    return (ano_atual - ano_nascimento) * 365

ano = int(input("Ano de nascimento: "))
print(f"Idade aproximada em dias: {calcula_idade_dias(ano)}")