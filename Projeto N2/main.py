"""Esse projeto tem como função criar um sistema que permite a inclusão, consulta, atualização,
e exclusão de produtos, além de exibir um relatório com a lista de produtos cadastrados.

Projeto N2

01J12 - BSI
Eduardo Hiroyuki Tamaributi - 32331762
Julia Kovacs Takamura - 
"""

def insira_codigo () :
    # Função para o usuário inserir o código do produto | Como o código foi utilizado diversas vezes, ele foi transformado em uma função
    while True :
        # Recebe um input do código do produto e caso ele possuir 4 dígitos, retorna o valor
        codigo = int(input("Código do produto: "))
        if codigo > 999 and codigo < 10000 :
            return codigo
        else :
            print('Erro! Código deve conter 4 dígitos\n')
        
def cadastra_produto () :
    # Cria um dicionário {produto} que possui as categorias: none, código e quantidade
    produto = {}
    produto['nome'] = input("Nome do produto: ")
    produto['code'] = insira_codigo()
    while True :
        produto['quant'] = int(input("Quant: "))
        if produto['quant'] > 0 :
            break
        else :
            print("Erro! Quant deve ser maior que 0\n")
    print(f'{produto["nome"]} cadastrado com sucesso\n')
    return produto

def consulta_produto (lista, codigo) :
    # Faz a consulta de um produto específico cadastrado
    for i in range (len(lista)) : # Itera entre os elementos da lista [estoque]
        if lista[i]['code'] == codigo : 
            # Caso o código do elemento for o mesmo que o parâmetro da função, printa esse elemento
            if len(lista[i]['nome']) > 6 :
                espacamento = len(lista[i]['nome']) - 6
                print('Produto', end='')
                print(' ' * espacamento, end='|')
                print(' Codigo | Quant')
            else :
                print('Produto| Codigo | Quant')
            print(f'{lista[i]["nome"]} |  {lista[i]["code"]}  | {lista[i]["quant"]}\n')
            break
    else :
        # Caso não haja correspondência para o código inserido como parâmetro, devolve uma mensagem de erro
        print("Erro! Produto não encontrado\n") 

def atualiza_produto (lista, codigo) :
    # Atualiza o nome e quantidade de um produto da lista [estoque]
    for i in range (len(lista)) : # Itera entre os elementos da lista [estoque]
        if lista[i]['code']== codigo : 
            # Caso o código do elemento for o mesmo que o parâmetro da função, atualiza o seu nome e/ou quantidade
            print(f'Produto a ser atualizado: {lista[i]["nome"]}')
            while True :
                att_nome = input("Deseja atualizar o nome (s/n): ")
                if att_nome.lower() == 's' :
                    lista[i]['nome'] = input("Nome atualizado: ")
                    break
                elif att_nome.lower() == 'n' :
                    break
                else :
                    print("Erro! Comando inválido\n")
            while True :
                att_quant = input("Deseja atualizar a quant (s/n): ")
                if att_quant.lower() == 's' :
                    lista[i]['quant'] = int(input("Quant atualizada: "))
                    break
                elif att_quant.lower() == 'n' :
                    break
                else :
                    print("Erro! Comando inválido\n")
            print(f'{lista[i]["nome"]} atualizado com sucesso\n')
            consulta_produto(lista, codigo)
            break
    else :
        # Caso não haja correspondência para o código inserido como parâmetro, devolve uma mensagem de erro
        print("Erro! Produto não encontrado\n") 

def excluir_produto (lista, codigo) :
    # Exclui um determinado elemento da lista [estoque]
    for i in range (len(lista)) : # Itera entre os elementos da lista [estoque]
        if lista[i]['code'] == codigo :
            # Caso o código do elemento for o mesmo que o parâmetro da função, pergunta se o usuário quer fazer a remoção do item
            while True :
                confirmar = input(f"Deseja remover o item {lista[i]['nome']} (s/n): ")
                if confirmar == 's' :
                    lista.pop(i)
                    print("Produto removido com sucesso\n")
                    break
                elif confirmar == 'n' :
                    print("Operação cancelada\n")
                    break
                else :
                    print('Erro! Comando inválido')
            break
    else :
        print("Erro! Produto não encontrado\n")

def exibe_relatorio (lista) :
    # Exibe um relatório do estoque apresentando o nome, código e quantidade de cada item
    if len(lista) > 0 :
        # Faz o cabeçalho do relatório
        espacamento = len(lista[0]['nome'])
        for i in range (len(lista)) :
            if len(lista[i]['nome']) > espacamento :
                espacamento = len(lista[i]['nome'])
        espacamento -= 7
        if espacamento < 0 : 
            espacamento = 0
        print('Produto', end='')
        print(' ' * espacamento, end='|')
        print(' Codigo | Quant')
        espacamento += 7
        for i in range (len(lista)) :
            # Printa os itens
            print(lista[i]['nome'], end='')
            print(' ' * (espacamento - len(lista[i]['nome'])), end='|')
            print(f'  {lista[i]["code"]}  |  {lista[i]["quant"]}')
        print()
    else :
        # Caso a lista [estoque] esteja vazia, retorna uma mensagem de erro
        print("Erro! Armazém vazio\n")

print('+++++++ MENU – CONTROLE DE ESTOQUE +++++++')
estoque = []
while True :
    # Printa as opções que o usuário possui
    print('1. Cadastrar Produto\n2. Consultar Produto\n3. Atualizar Produto\n4. Excluir Produto\n5. Relatório de Produtos\n6. Encerrar')
    escolha = int(input("Opção escolhida: "))
    print()
    if escolha == 6 : 
        break
    elif escolha == 1 :
        estoque.append(cadastra_produto())
    elif escolha == 2 :
        consulta_produto(estoque, insira_codigo())
    elif escolha == 3 :
        atualiza_produto(estoque, insira_codigo())
    elif escolha == 4 :
        excluir_produto(estoque, insira_codigo())
    elif escolha == 5 :
        exibe_relatorio(estoque)
    else :
        print("Erro! Comando inválido\n") 