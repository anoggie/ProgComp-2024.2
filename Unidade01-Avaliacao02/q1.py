# questão 1 - Contador de números decrescentes de 10 a 987631
# by Anielly & Israel

inicial = 10 # número inicial
final = 987631 # número final
contador = 0

for num in range(inicial, final + 1): # itera sobre todos os números de 10 a 987631
    decrescente = True

    while num >= 10: # verifica se o número é decrescente pegando os dois últimos dígitos
        ultimo_digito = num % 10
        num = num // 10
        penultimo_digito = num % 10

        if penultimo_digito < ultimo_digito: # compara se o penúltimo é menor que o último
            decrescente = False
            break # se não for, para a iteração

    if decrescente: # se o número for decrescente, incrementa ao contador
        contador += 1

print(f"O total de números decrescentes de {inicial} a {final} é: {contador}")