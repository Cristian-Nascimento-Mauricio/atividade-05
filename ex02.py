"""
    2- Verificador de Palíndromos
    Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

    *Solicite ao usuário uma palavra ou frase.
    *Desconsidere letras maiúsculas, espaços e sinais de pontuação.
    *Verifique se a frase é um palíndromo.
    *Exiba "Sim" se for palíndromo ou "Não" se não for.

    Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
"""

def verifica_palindromo(texto):
    filtrado = ''.join(c.lower() for c in texto if c.isalnum())
    return filtrado == filtrado[::-1]

entrada = input("Digite uma palavra ou frase: ")
print("Sim" if verifica_palindromo(entrada) else "Não")
