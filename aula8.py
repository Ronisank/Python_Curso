from datetime import datetime;

data_hoje = datetime.now()
nome = 'Roni'
sobrenome = 'Santos'
idade = 39
ano_nascimento =  data_hoje.year - idade
maior_idade = idade >= 18
altura_metros = 1.79

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento', ano_nascimento)
print('Maior idade:', maior_idade)
print('Altura em metros:', altura_metros)

