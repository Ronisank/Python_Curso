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
lista = ["A", "B", "C", "D"]
for pergunta in perguntas:
    print(f'{pergunta["Pergunta"]}', "\n")
    print("Opções: ")
    for opcao in enumerate(pergunta["Opções"]):
        # print(lista[opcao[0]], ")", opcao[1])
