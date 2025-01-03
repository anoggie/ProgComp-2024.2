# questão 3 - Term.ooo
# by Anielly & Israel

import random

# Configuração de cores para feedback visual
cor_def = '\033[0;0m'  # Cor padrão
non_existent = '\033[40m'  # Fundo preto, letra não existe na palavra
wrong_pos = '\033[43m'  # Fundo amarelo, letra está na palavra mas em posição errada
correct_pos = '\033[42m'  # Fundo verde, letra está correta e na posição certa

# Lista de palavras possíveis para o jogo
palavras = ("ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
            "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
            "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
            "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
            "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
            "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
            "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
            "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
            "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
            "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
            "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
            "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
            "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
            "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
            "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
            "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
            "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
            "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
            "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
            "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA")

# Sorteio de duas palavras diferentes da lista
palavra_1 = random.choice(palavras)
palavra_2 = random.choice(palavras)

# Garantir que as duas palavras sejam diferentes
p1 = palavra_1
p2 = palavra_2

while palavra_2 == palavra_1:
    palavra_2 = random.choice(palavras)

# Variáveis de controle do jogo
fim_do_jogo = False
tentativas = 7  # Número de tentativas que o jogador tem para acertar as palavras

# Exibição de instruções iniciais
print('=' * 100)
print('BEM VINDO AO TERMO!')
print('Você deve descobrir as palavras corretas. A cada tentativa, você verá o quão perto estará da solução.')
print(correct_pos + 'A' + cor_def + 'DAGA -> a letra  "A" faz parte da palavra e está na posição correta')
print('VE' + wrong_pos + 'N' + cor_def + 'TO -> a letra "N" faz parte da palavra, mas em outra posição')
print('PUL' + non_existent + 'G' + cor_def + 'A -> a letra "G" não faz parte da palavra')
print('As palavras podem possuir letras repetidas!')
print('=' * 100)

# Debug: exibe as palavras sorteadas
#print(palavra_1, palavra_2)

# Loop principal do jogo
while fim_do_jogo == False:
    chute = input("Digite uma palavra (5 letras): ").upper()[:5]  # Chute
    
    # Verificação se o chute está na lista de palavras válidas
    if chute not in palavras:
        print("Essa palavra não está na lista de palavras válidas. Tente novamente.")
        continue  # Volta para o início do loop sem descontar tentativas

    tentativas -= 1

    # Verificação de vitória: se o chute for igual a uma das palavras
    acertou_1 = chute == palavra_1
    acertou_2 = chute == palavra_2

    if acertou_1:
        print(f"Você acertou a primeira palavra: {palavra_1}")
        palavra_1 = None  # Marcar como resolvida
    if acertou_2:
        print(f"Você acertou a segunda palavra: {palavra_2}")
        palavra_2 = None  # Marcar como resolvida

    # Verificar se o jogo acabou
    if palavra_1 is None and palavra_2 is None:
        if tentativas == 6:
            print("Impossível")
        elif tentativas == 5:
            print("Ninja")
        elif tentativas == 4:
            print("Impressionante")
        elif tentativas == 3:
            print("Interessante")
        elif tentativas == 2:
            print("Pode melhorar")
        elif tentativas == 1:
            print("Foi por pouco")

        fim_do_jogo = True  # Fim do jogo

    elif tentativas == 0:
        print(f"Acabaram as chances. As palavras eram {p1} e {p2}.")
        fim_do_jogo = True  # Fim do jogo

    # Feedback visual do chute
    if not fim_do_jogo:
        feedback_1 = ""
        feedback_2 = ""
        for i in range(len(chute)):
            letra = chute[i]
            # Feedback para a primeira palavra
            if palavra_1 and i < len(palavra_1):
                if letra == palavra_1[i]:
                    feedback_1 += correct_pos + letra + cor_def  # Letra correta e na posição certa
                elif letra in palavra_1:
                    feedback_1 += wrong_pos + letra + cor_def  # Letra existe, mas em posição errada
                else:
                    feedback_1 += non_existent + letra + cor_def  # Letra não existe
            # Feedback para a segunda palavra
            if palavra_2 and i < len(palavra_2):
                if letra == palavra_2[i]:
                    feedback_2 += correct_pos + letra + cor_def  # Letra correta e na posição certa
                elif letra in palavra_2:
                    feedback_2 += wrong_pos + letra + cor_def  # Letra existe, mas em posição errada
                else:
                    feedback_2 += non_existent + letra + cor_def  # Letra não existe
        # Exibir feedback para ambas as palavras
        print(f"Palavra 1: {feedback_1}")
        print(f"Palavra 2: {feedback_2}")
