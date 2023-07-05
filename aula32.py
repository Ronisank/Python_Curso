"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')
# try:
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'O número {numero_int} é par')
#     else:
#         print(f'O número {numero_int} é ímpar')
# except:
#     print('Você não digitou um número, não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Solução 1
# bom_dia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
# boa_tarde = [12, 13, 14, 15, 16, 17]
# boa_noite = [18, 19, 20, 21, 22, 23]
# entrada = input('Digite a hora: ')

# try:
#     hora = int(entrada)
#     if hora in bom_dia[0:12]:
#         print('Bom dia')
#     elif hora in boa_tarde[0:6]:
#         print('Boa tarde')
#     elif hora in boa_noite[0:6]:
#         print('Boa noite')
#     else:
#         print('Você não digitou uma hora válida, Digite entre 0 e 23 horas')
# except:
#     print('Você não digitou uma hora válida, digite números inteiros')

# Solução 2
# entrada = input('Digite a hora: ')
# try:
#     hora = int(entrada)
#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Você não digitou uma hora válida, Digite entre 0 e 23 horas')
# except:
#     print('Digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
nome_tamanho = len(nome)

if nome_tamanho > 1:
  if nome_tamanho <= 4:
    print('Seu nome é curto')
  elif len(nome) <= 6:
    print('Seu nome é normal')
  else:
    print('Seu nome é muito grande')
else:
  print('Digite mais de uma letra')