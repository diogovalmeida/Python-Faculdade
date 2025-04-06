# Crie uma função que receba uma lista de números e retorne a média aritmética

def mediaaritmetica():
    n = int(input("Escreva o nº de números que queres: "))
    numeros = []

    for i in range(n):
        numero = int(input(f"Selecione o nº{i + 1}: "))
        numeros.append(numero)

    soma = sum(numeros)
    media = soma / len(numeros)
    print("A média dos números é:", media)

mediaaritmetica()