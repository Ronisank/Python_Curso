nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if nome and idade:
    nome = nome.upper()
    print(f'Seu nome é: {nome} e possui {idade} anos.')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços em branco.')
    else:
        print(f'Seu nome NÃO contém espaços em branco.')
    print(f'Seu nome tem {len(nome)} caracteres.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')