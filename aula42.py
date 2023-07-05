frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guidovan Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_mais_repetida = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    print(f'Letra "{letra_atual}" apareceu {qtd_apareceu_mais_vezes_atual}x')

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_mais_repetida = letra_atual

    i += 1
    
print('A letra que apareceu mais vezes foi '
    f'"{letra_mais_repetida}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x')