# Escreva uma função que verifique se um número é um palíndromo (Capicua)

def palindromo(numero):
    numero_str = str(numero) # Converte o nº em String
    return numero_str == numero_str[::-1] # Inverte a String. O "==" é a comparação e pode retornar True ou Falso


numero_digitado = input("Digite um número: ")

if palindromo(numero_digitado):
    print("É um palíndromo (capicua).") # Se True
else:
    print("Não é um palíndromo.") # Se False
