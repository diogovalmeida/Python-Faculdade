# Escreva uma função que verifique se um número é par ou ímpar

def validacao():
    n = int(input("Escreva o nº: "))

    if n % 2 == 0:
        print("É par")
    else:
        print("É impar")

validacao()