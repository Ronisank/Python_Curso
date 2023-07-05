# import copy

"""Aula 76 - Dicionários em Python - parte 1"""

# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# pessoa = {
#     "nome": "Luiz Otávio",
#     "sobrenome": "Miranda",
#     "idade": 18,
#     "altura": 1.8,
#     "endereços": [
#         {"rua": "tal tal", "número": 123},
#         {"rua": "outra rua", "número": 321},
#     ],
# }
# # print(pessoa, type(pessoa))
# print(pessoa["nome"])
# print(pessoa["sobrenome"])

# print()

# for chave in pessoa:
# print(chave, pessoa[chave])

"""
Aula 76 - Métodos úteis dos dicionários em Python - parte 2
    Manipulando chaves e valores em dicionários
"""
# pessoa = {}

# ##
# ##

# chave = "nome"

# pessoa[chave] = "Luiz Otávio"
# pessoa["sobrenome"] = "Miranda"


# print(pessoa[chave])

# pessoa[chave] = "Maria"

# del pessoa["sobrenome"]
# print(pessoa)
# print(pessoa["nome"])

# # print(pessoa.get('sobrenome'))
# if pessoa.get("sobrenome") is None:
#     print("NÃO EXISTE")
# else:
#     print(pessoa["sobrenome"])

# print('ISSO Não vai')

"""
Aula 76 - Métodos úteis dos dicionários em Python - parte 3
        Métodos úteis dos dicionários em Python
"""
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     "nome": "Luiz Otávio",
#     "sobrenome": "Miranda",
#     "idade": 900,
# }

# pessoa.setdefault("idade", 0)
# print(pessoa["idade"])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

"""
Aula 76 - Métodos úteis dos dicionários em Python - parte 4
        Métodos úteis dos dicionários em Python
    Shallow Copy vs Deep Copy em dados mutáveis em Python
"""

# d1 = {
#     "c1": 1,
#     "c2": 2,
#     "l1": [0, 1, 2],
# }

# d3 = {
#     "c1": 1,
#     "c2": 2,
#     "l1": [0, 1, 2],
# }
# d2 = copy.deepcopy(d1)  # Faz uma cópia profunda
# d4 = d1.copy()  # Faz uma cópia rasa

# d2["c1"] = 1000
# d2["l1"][1] = 999999

# print(d1)
# print(d2)

"""
Aula 76 - Métodos úteis dos dicionários em Python - parte 5
        Métodos úteis dos dicionários em Python
"""

# p1 = {
#     "nome": "Luiz",
#     "sobrenome": "Miranda",
# }
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [["nome", "novo valor"], ["idade", 30]]
# p1.update(lista)
# print(p1)
