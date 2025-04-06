# Implemente uma função que receba uma lista e retorna uma nova lista com os elementos invertidos

import random

def lista_aleatoria():
    n = int(input("Escreva o nº de números que queres: "))
    numeros = []

    for i in range(n):
        numero = int(input(f"Selecione o nº{i + 1}: "))
        numeros.append(numero)

    random.shuffle(numeros)
    print(numeros)

lista_aleatoria()