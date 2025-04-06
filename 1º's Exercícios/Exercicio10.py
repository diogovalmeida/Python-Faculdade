# Implemente uma função recursiva para calcular o n-ésimo número da sequência de Fibonacci
# Fórmula: F(n)=F(n−1)+F(n−2)

def fibonacci(n):
    if n >= 30:
        raise ValueError("O valor é muito grande! A sequência de Fibonacci vai estragar o código.")
    elif n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    num = int(input("Digite a posição da sequência de Fibonacci: "))
    resultado = fibonacci(num)
    print(f"O {num}º número da sequência de Fibonacci é: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")