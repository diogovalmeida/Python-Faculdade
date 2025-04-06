# Se estão Ordenados ou Não estão Ordenados

def sessao():
    try:
        n = int(input("Escreva o nº de números que queres: "))
        numeros = []

        for i in range(n):
            numero = int(input(f"Selecione o nº{i + 1}: "))
            numeros.append(numero)

        if numeros == sorted(numeros):
            print("Ordenados")
        else:
            print("Não ordenados")
            numeros.sort()
            print("Lista ordenada:", numeros)
    except ValueError:
        print("Erro: Por favor, insere apenas números inteiros.")



sessao()