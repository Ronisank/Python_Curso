#Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
print ('Exercício 1')
print ('')
def multiplica(*args):
    total = 1
    for i in args:
        total *= i
    return total

resultado = multiplica(1,2,3,4,5,6)
print (resultado)

print('Exercício 2')
print ('')
def par_ou_impar(num):
    if num % 2 == 0:
        return 'PAR'
    return 'IMPAR'
    
numero = int(input('Digite um número: '))    
    
print (par_ou_impar(numero))