"""Possíveis problemas e soluções para nosso algoritmo do CPF"""

import re # Expressão regular
import sys
import random

entrada = input('[1]Gerar um CPF --- [2] Validar CPF --- ')
nove_digitos = ''

if entrada == '1': 
    numeros = '' 
    for i in range(9):
        numeros += str(random.randint(0, 9))
elif entrada == '2':
    cpf_enviado_usuario = re.sub(r'[^0-9]','',input("Digite seu CPF, apenas números: "))

    entrada_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

    if entrada_sequencial:
        print('Você digitou dados sequenciais')
        sys.exit()    
else:
    print('Entrada inválida')
    sys.exit()
if entrada == '1':
   nove_digitos = numeros
else:
    nove_digitos = cpf_enviado_usuario[:9]   

#Validando o primeiro digito do CPF

indice_regressivo = 10
resultado_digito_1 = 0

for num, in nove_digitos:
  resultado_digito_1 += int(num) * indice_regressivo
  indice_regressivo -= 1
  

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

## Validando o segundo digito do CPF

dez_digitos = nove_digitos + str(digito_1)
indice_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * indice_regressivo_2
    indice_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
cpf_gerado_no_calculo = f'{nove_digitos}{digito_1}{digito_2}'

cpf_enviado_usuario = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_no_calculo:
    print(f'{nove_digitos}{digito_1}{digito_2}')
    print('CPF Válido')
else:
    print('CPF inválido')