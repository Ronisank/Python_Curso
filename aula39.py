"""
Iterando strings com while em Python
"""
#.......012345678910
nome = 'Roni Santos' # Iteráveis
tamanho = len(nome)
print(tamanho)
novo_nome = ''
cont = 0

while cont <= 10:
    letra = nome[cont]
    novo_nome += f'*{letra}'    
    cont += 1
    
novo_nome += '*'
print(novo_nome)
    
    

