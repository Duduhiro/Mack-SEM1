""" Escreva um programa que leia 10 dados no formato caractere que representa o gabarito de
uma prova com 10 questões. Armazene os caracteres lidos em uma lista. A seguir, para cada
um dos 15 alunos de uma turma, leia o nome e o vetor de respostas (R) do aluno. Após ler,
conte o número de acertos e ARMAZENE em uma lista de resultados o NOME e a NOTA FINAL
desse aluno. Faça isso para todos os alunos. Após esse processamento das notas, mostre o
nome do aluno e a NOTA FINAL seguida da mensagem APROVADO, se a nota FINAL for maior
ou igual a 6 ou seguida da mensagem REPROVADO, caso contrário. """

gabarito = []
for i in range (10) :
    while True :
        quest = input(f"Questão{i + 1}: ")
        if len(quest) == 1 :
            gabarito.append(quest)
            break
        else :
            print("Invalid Command!")
alunos = []
for i in range (3) :
    aluno = {
        'aprovado': 'REPROVADO',
        'final': 0,
    }
    respostas = []
    aluno['name'] = input(f"(Student {i + 1}) Name : ")
    for j in range (10) :
        while True :
            bacon = input(f"Questão{j + 1}: ")
            if len(bacon) == 1 :
                respostas.append(bacon)
                break
            else :
                print("Invalid Command!")
    aluno['respostas'] = respostas
    alunos.append(aluno)

for i in range (len(alunos)) :
    acerto = 0
    for j in range (len(gabarito)) :
        if gabarito[j] == alunos[i]['respostas'][j] :
            acerto += 1
    alunos[i]['final'] = acerto
    if acerto >= 6 :
        alunos[i]['aprovado'] = 'APROVADO'
print()

for i in range (len(alunos)) :
    print(f"{alunos[i]['name']} | Nota: {alunos[i]['final']} | {alunos[i]['aprovado']}")