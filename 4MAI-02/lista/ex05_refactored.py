""" 5) Faça um programa que peça quatro notas de 4 alunos como valores reais entre 0 e 10,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos
aprovados com média maior ou igual a 7.0. Implemente três funções, uma primeira de
entrada para ler cada nota, validar se cada nota está no intervalo entre 0 e 10 e inserir a
média de cada aluno em um vetor. Uma segunda função para verificar e contabilizar
quantos alunos estão aprovados. Uma terceira função para imprimir as médias dos alunos
e a quantidade de alunos aprovados, esta última função possui um argumento contendo
o número de alunos aprovados. Dica: utilize a função append() em python para inserir
elementos no vetor.  """

""" Como alteração do programa inicial, a versão refactored irá registrar indeterminados alunos e além das médias,
irá também registrar os nomes e notas e salva-las em um dicionário {nome, n1, n2, n3, n4, media, aprovado} 

v2. Adicionei uma função para pesquisar um aluno em específico a partir de seu nome depois de mostrado a tabela inteira
"""

def registra_aluno () :
    # Essa função registra uma indeterminada quantidade de alunos em uma lista
    lista_alunos = []
    while True :
        aluno = {'name': '', 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 'grad': ''} # As características de um aluno são Nome, n1, n2, n3, n4, média, aprovação
        name = input("Student Name (q - exit): ")
        if name.lower() == 'q' :
            break
        aluno['name'] = name
        scores = []
        for i in range (4) :
            # Registra as 4 notas de um aluno
            while True :
                n = float(input(f"N{i + 1} - {name}: "))
                if n >= 0 and n <= 10 :
                    break
                print("Error!")
            scores.append(n)
        for j in range (4) :
            aluno[j + 1] = scores[j]
        aluno[5] = sum(scores) / 4 # Calcula a média do aluno 
        if sum(scores) / 4 >= 7 : # Verifica se o aluno foi reprovado ou aprovado
            aluno['grad'] = 'Pass'
        else :
            aluno['grad'] = 'Failed'
        lista_alunos.append(aluno) # Registra as informações do aluno na lista de alunos
    return lista_alunos

def imprime_boletin (lista) :
    print('Name      |  G1  |  G2  |  G3  |  G4  |  AVG | Pass/Fail') # Printa o header da tabela
    for i in range (len(lista)) :
        spaces = 10 - len(lista[i]['name']) # Calcula quantos espaços são necessários de identação na área do nome
        print(f"{lista[i]['name']}", end="") 
        print(f" " * spaces, end="|")
        for j in range (1, 6) :
            #Printa as notas e média
            if lista[i][j] == 10 :
                print(f' {lista[i][j]:3.1f} |', end='')
            else :
                print(f' {lista[i][j]:3.2f} |', end='')
        print(f' {lista[i]["grad"]}') # Printa se o aluno foi aprovado ou reprovado
    print()
    
def search_student (lista, nome) :
    # Procura um aluno em específico na lista de alunos
    for i in range (len(lista)) :
        if lista[i]['name'] == nome :
            print('Name      |  G1  |  G2  |  G3  |  G4  |  AVG | Pass/Fail')
            spaces = 10 - len(lista[i]['name'])
            print(f"{lista[i]['name']}", end="")
            print(f" " * spaces, end="|")
            for j in range (1, 6) :
                if lista[i][j] == 10 :
                    print(f' {lista[i][j]:3.1f} |', end='')
                else :
                    print(f' {lista[i][j]:3.2f} |', end='')
            print(f' {lista[i]["grad"]}')
            while True :
                edit = input("Edit this student grade (y/n): ")
                if edit.lower() == 'n' :
                    break
                elif edit.lower() == 'y' :
                    while True :
                        grade = int(input("Grade 1 | 2 | 3 | 4 : "))
                        if grade >= 1 and grade <= 4 :
                            break
                    while True :
                        grade_value = float(input("Grade: "))
                        if grade_value >= 0 and grade_value <= 10 :
                            break
                    edita_aluno(lista, i, grade, grade_value)
                    print('Grade Updated Sucessfully\n')
                    search_student(lista, nome)
                    break
                else :
                    print("Error! Wrong command\n")
            break
    else :
        print('Wrong Name')

def edita_aluno (lista, student_number, grade, grade_value) :
    lista[student_number][grade] = grade_value
    grade_sum = 0
    for i in range (1, 5) :
        grade_sum += lista[student_number][i]
    lista[student_number][5] = grade_sum / 4
    if (grade_sum / 4) >= 7 :
        lista[student_number]['grad'] = 'Pass'
    else :
        lista[student_number]['grad'] = 'Failed'

lista_alunos = registra_aluno()
print()
imprime_boletin(lista_alunos)
while True :
    # Pergunta ao usuário se ele quer pesquisar um aluno em específico
    search = input("Search individual Student (y/n): ")
    if search.lower() == 'y' :
        # Pesquisa os dados do aluno a partir de seu nome
        student_name = input("Student Name: ")
        print()
        search_student(lista_alunos, student_name)
        print()
        imprime_boletin(lista_alunos)
    elif search.lower() == 'n' :
        break
    else :
        print("Error! Wrong Usage")