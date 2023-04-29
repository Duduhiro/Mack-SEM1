import csv
lista_funcionarios = []

def hora_funcionario (nome, horas) :
    funcionario = {
        "nome": nome,
        "horas": horas
    }
    return funcionario

while True :
    nome = input("Nome (q - para sair): ")
    if nome.lower() == "q" :
        break
    horas = float(input("Horas: "))
    lista_funcionarios.append(hora_funcionario(nome, horas))

for i in range (len(lista_funcionarios)) :
    print(f"Funcionário {i + 1}: ")
    print(f"    Nome: {lista_funcionarios[i]['nome']}")
    print(f"    Horas: {lista_funcionarios[i]['horas']}")

header = ['nome', 'hora']
csvfile = 'hora_funcionario.csv'
with open (csvfile) as file :
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(lista_funcionarios)
