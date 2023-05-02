""" 5) Faça um programa que peça quatro notas de 4 alunos como valores reais entre 0 e 10,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos
aprovados com média maior ou igual a 7.0. Implemente três funções, uma primeira de
entrada para ler cada nota, validar se cada nota está no intervalo entre 0 e 10 e inserir a
média de cada aluno em um vetor. Uma segunda função para verificar e contabilizar
quantos alunos estão aprovados. Uma terceira função para imprimir as médias dos alunos
e a quantidade de alunos aprovados, esta última função possui um argumento contendo
o número de alunos aprovados. Dica: utilize a função append() em python para inserir
elementos no vetor.  """

def cadastra_notas () :
    media = []
    for j in range (4) :
        notas = 0
        for i in range (4) :
            while True :
                nota = float(input(f"Nota {i + 1} - aluno {j + 1}: "))
                if nota >= 0 and nota <= 10 :
                    break
            notas += nota
        media.append(notas / 4)
    return media

def verifica_aprovados (media) :
    aprovados = 0
    for i in range (len(media)) :
        if media[i] >= 7 :
            aprovados += 1
    return aprovados

def imprime (media, aprovados) :
    print(media)
    print(f"Aprovados: {aprovados}")

medias = cadastra_notas()
aprovados = verifica_aprovados(medias)
imprime(medias, aprovados)