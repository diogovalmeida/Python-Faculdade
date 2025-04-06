# Crie uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra

def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem


def palavras_todas():
    p = int(input("Escreva o nº de palavras que queres: "))
    palavras = []

    for i in range(p):
        while True:
            try:
                palavra = input(f"Digite a palavra nº {i + 1}: ")
                if not palavra.isalpha():
                    raise ValueError("Só é permitido letras. Tenta outra vez!")
                palavras.append(palavra)
                break
            except ValueError as e:
                print(f"Erro: {e}")
    return palavras


palavras2 = palavras_todas()
resultado = contar_palavras(palavras2)
print(resultado)