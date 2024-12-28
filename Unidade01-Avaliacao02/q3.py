# questão 3 - Pares de primos ímpares consecutivos < 1000000
# by Anielly & Israel

limite = 1000000 # limite superior
primeiro_impar = 3 # inicializa o primeiro ímpar
pares = 0

for n in range(5, limite, 2):
    primo = True # assume que n é primo de primeira

    for i in range(2, int(n**0.5) + 1): # verifica se n é primo
        if n % i == 0:
            primo = False # se n for divisível por i, n não é primo
            break

    if primo:
        if n - primeiro_impar == 2: # verifica se a diferença entre os ímpares é 2
            pares += 1 # incrementa a quantidade de pares encontrados
        primeiro_impar = n

print(f'Quantidade de pares: {pares}')