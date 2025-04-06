# Crie uma função que calcule o fatorial de um número

def fat(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

n = int(input("Escreva o seu nº: "))
resultado = fat(n)
print(f"O fatorial de {n} é: {resultado}")