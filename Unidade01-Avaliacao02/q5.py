# questão 5 - Quantos sábados ocorreram entre 27/04/1968 e a data atual?
# by Anielly e Israel

import datetime

# data atual
date = datetime.datetime.today()
dia_atual = date.day
mes_atual = date.month
ano_atual = date.year

# data inicial
diazero = 27
meszero = 4
anozero = 1968

# contadores
diaspassados = 0
totalsabados = 0

# enquanto a data inicial for menor ou igual à data atual...
while anozero < ano_atual or (anozero == ano_atual and meszero < mes_atual) or (anozero == ano_atual and meszero == mes_atual and diazero <= dia_atual):
    # incrementa o contador de dias
    diaspassados += 1

    # vê se é um sábado
    if diaspassados % 7 == 0:
        totalsabados += 1

    # incrementa o dia
    diazero += 1

    # valida se o mês de fevereiro é bissexto ou não, e define o número de dias de cada mês
    if meszero == 2: # fevereiro
        bissexto = (anozero % 400 == 0) or (anozero % 4 == 0 and anozero % 100 != 0)
        diasmes = 29 if bissexto else 28
        
    elif meszero == 4 or meszero == 6 or meszero == 9 or meszero == 11: # abril, junho, setembro, novembro
        diasmes = 30
    else:  # outros meses
        diasmes = 31

    # se o dia for maior que o número de dias do mês, vai para o próximo mês e reseta o dia para 1º
    if diazero > diasmes:
        diazero = 1
        meszero += 1
        if meszero > 12:
            meszero = 1
            anozero += 1

print(f'Total de sábados entre 27/4/1968 até {dia_atual}/{mes_atual}/{ano_atual} é: {totalsabados}')