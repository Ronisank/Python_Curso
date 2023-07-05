#### Calculadora While ####
while True:  
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite um operador: [+, -, *, /] ')

    numeros_validos = None
    num1_= 0
    num2_= 0
    try:
        num1 = float(numero1)
        num2 = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if operador == '+':
            print(f'A Soma de {num1} + {num2} =  {num1 + num2:.2f}' )
    elif operador == '-':
            print(f'A Subtração de {num1} - {num2} =  {num1 - num2:.2f}' )
    elif operador == '*':
            print(f'A Multiplicação de {num1} * {num2} =  {num1 * num2:.2f}' )
    elif operador == '/':
            print(f'A Divisão de {num1} / {num2} =  {num1 / num2:.2f}' )
    elif operador != '+' or operador != '-' or operador != '*' or operador != '/':
            print('Operador inválido.') 

    sair = input('Deseja sair? [S]im ').upper().startswith('S')      
    
    if sair is True:
        break
            
