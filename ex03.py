"""
    3- Calculadora de Desconto em Produto
    Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

    * Solicitar o preço original do produto.  
    * Solicitar o percentual de desconto desejado.  
    * Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def calcula_preco_com_desconto(preco, desconto_percentual):
    return preco * (1 - desconto_percentual / 100)

preco_original = float(input("Preço original do produto: R$ "))
percentual = float(input("Percentual de desconto (%): "))
preco_final = calcula_preco_com_desconto(preco_original, percentual)
print(f"Preço final com desconto: R$ {preco_final:.2f}")