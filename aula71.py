"""args - Argumentos não nomeados
* - *args (empacotamentos e desempacotamentos)
"""

# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4, 5, 6
# print(x, y, resto)

## Exemplo 
def soma(*args):
    total = 0
    for n in args:
        total += n        
    return total
    
resultado = soma(1, 2, 3, 4, 5, 6)
print(resultado)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

# desempacotamento
outra_soma = soma(*numeros)
print(outra_soma, 'pegando da função soma')

print(sum(numeros), 'pegando da função sum')    