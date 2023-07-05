import os

lista_compra = []

while True:
    print('Selecione uma opção:')
    opcao = input('[I]nserir item [A]pagar item  [L]istar [S]air ').upper()
    try:
        if opcao == 'A' and not len(lista_compra):
            os.system('cls')
            print('Não há itens na lista!')
            continue    
        if opcao == 'L' and not len(lista_compra):
            os.system('cls')
            print('A lista está vazia!')
            continue
        if opcao != 'I' and opcao != 'A' and opcao != 'L' and opcao != 'S':
            print('Opção inválida! do try')
            continue
            
    except:
        print('Erro inesperado!')
        continue

    if opcao == 'I':        
        item = input('Digite o item a ser inserido: ')
        lista_compra.append(item)
        os.system('cls')
    elif opcao == 'A' and len(lista_compra):        
        item = input('Digite o indice a ser apagado: ')
        for indice, item_lista in enumerate(lista_compra):
            item = int(item)
            print(indice, item_lista)
            if indice == item:
                os.system('cls')
                del lista_compra[indice]
                print('Item apagado!')
            else:
                os.system('cls')  
                print('Item não encontrado!')                                    
    elif opcao == 'L':
        for indice, item in enumerate(lista_compra):
            print(indice, item)
    elif opcao == 'S':
        break
    else:
        print('Opção inválida!')
print('Fim do programa!')