# questão 2 - Quantidade de números palíndromos entre 10 e 100000
# by Anielly & Israel

contador = 0 # inicializa o contador de palíndromos

for i in range(10, 100001): # percorre os números de 10 a 100000
    original = i # guarda o valor original
    reverso = 0 # guarda o valor reverso

    while i > 0: # inverte o número
        ultimo_digito = i % 10 # pega o último dígito
        reverso = reverso * 10 + ultimo_digito # constrói o número reversamente
        i = i // 10 # remove o último dígito

    if original == reverso: # verifica se o número é palíndromo
        contador += 1 # incrementa ao contador

print(contador)

'''
NOTA DOS DEVS: Essa questão poderia ter sido feita de duas formas, uma onde definiriamos variáveis para não ficar mexendo nos laços:

    inicial = 10
    teto = 100000 + 1 (o + 1 serve para não dar errado no range)

    for i in range(inicial, teto):
    
A segunda maneira, é a que está feita na questão, que definimos o range diretamente no laço.
'''