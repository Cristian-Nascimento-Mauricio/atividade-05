"""
    1- Calculadora de Gorjeta
    Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

    * Defina o valor da conta (ex: R$ 100,00).  
    * Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
    * O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

def calcular_gorjeta(total_conta, porcentagem):
    return total_conta * (porcentagem / 100.0)

total_conta = float(input("Digite o valor total da conta (ex: 100.00): R$ "))
    
porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10): "))
    
valor_gorjeta = calcular_gorjeta(total_conta, porcentagem)
    
print(f"Para uma conta de R$ {total_conta:.2f} e gorjeta de {porcentagem:.0f}%, "
      f"o valor da gorjeta é R$ {valor_gorjeta:.2f}.")