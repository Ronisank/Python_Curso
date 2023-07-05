# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplo(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = multiplo(2)
triplicar = multiplo(3)
quadruplicar = multiplo(4)

lista = (10, 15, 30)

for numeros in lista:
    print(duplicar(numeros), "Numero duplicado de ", numeros)
    print(triplicar(numeros))
    print(quadruplicar(numeros))
