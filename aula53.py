"""
Enumerate - enumera iteravéis (listas, tuplas, strings)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

for indice, nome in enumerate(lista):
    print(lista[0], nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome, item)


# for tupla_enumerada in enumerate(lista):
#     print("FOR da tupla:")
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")


# for i in range(51):
#     print(i, '-',end=' ')
# print()
# print('*'*130)

# for i in range(51,101):
#     print(i,'-', end=' ')
# print()
# print('*'*130)

# for i in range(101,151):
#     print(i, '-',end=' ')
# print()
# print('*'*130)

# for i in range(151,201):
#     print(i,'-',end=' ')
# print()
# print('*'*130)
