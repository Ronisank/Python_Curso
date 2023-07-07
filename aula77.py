# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]
print(len(perguntas))
respostas_certas = 0

for pergunta in perguntas:
    print(f'{pergunta["Pergunta"]}', "\n")
    print("Opções: ")
    for indice, opcao in enumerate(pergunta["Opções"]):
        print(f"{indice}) {opcao}")
    resposta = input("Digite a opção correta: ")
    if pergunta["Opções"][int(resposta)] == pergunta["Resposta"]:
        respostas_certas += 1
        print("Você acertou!")
    else:
        print("Você errou!")
    print()
print(f"Você acertou {respostas_certas} de {len(perguntas)} perguntas.")
