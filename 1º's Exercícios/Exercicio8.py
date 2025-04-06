# Crie uma função que simule o lançamento de um dado de 6 faces e retorne o resultado

import random

def lancamento():
    dado = [1,2,3,4,5,6]

    x = random.choice(dado)
    print(x)

lancamento()