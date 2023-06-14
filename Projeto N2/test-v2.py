"""
Projeto N2

01J12 - BSI
Eduardo Hiroyuki Tamaributi - 32331762
Julia Kovacs Takamura - 32371489
"""
from tabulate import tabulate
import sqlite3

conn = sqlite3.connect('p2.db')
cursor = conn.cursor()

def int_input (msg) :
    while True :
        try :
            number = int(input(msg))
            break
        except ValueError :
            print("Invalid input. Please enter a integer")
    return number

def insira_codigo () :
    # Função para o usuário inserir o código do produto | Como o código foi utilizado diversas vezes, ele foi transformado em uma função
    while True :
        # Recebe um input do código do produto e caso ele possuir 4 dígitos, retorna o valor
        codigo = int_input("Código do produto: ")
        if codigo >= 0 and codigo < 10000 :
            return codigo
        else :
            print('Erro! Código deve conter no máximo 4 dígitos\n')
        
def cadastra_produto () :
    # Cria um dicionário {produto} que possui as categorias: none, código e quantidade
    cursor.execute("SELECT code FROM storage")
    code_list = cursor.fetchall()
    produto = {}
    produto['nome'] = input("Nome do produto: ")
    while True :    
        produto['code'] = insira_codigo()
        for i in code_list :    
            if produto['code'] in i :
                print('Error! Code already used\n')
                break
        else :
            break         
    while True :
        produto['quant'] = int_input("Quant: ")
        if produto['quant'] > 0 :
            break
        else :
            print("Erro! Quant deve ser maior que 0\n")
    cursor.execute("INSERT INTO storage (product, code, quant) VALUES (?, ?, ?)", (produto['nome'], produto['code'], produto['quant']))
    print(f'{produto["nome"]} cadastrado com sucesso\n')
    
def consulta_produto (codigo) :
    cursor.execute("SELECT product, code, quant FROM storage WHERE code = ?", (codigo,))
    product = cursor.fetchall()
    if len(product) > 0 :
        headers = [description[0] for description in cursor.description]
        print(tabulate(product, headers=headers, tablefmt="simple_grid"))
    else :
        print("Product Not Found!\n")

def atualiza_produto (codigo) :
    # Atualiza o nome e quantidade de um produto da lista [estoque]
    cursor.execute("SELECT product, code, quant FROM storage WHERE code = ?", (codigo,))
    product = cursor.fetchall()
    if len(product) > 0 :
        consulta_produto(codigo)
        while True :
            update = input("Do you want to update this item's name (y/n): ")
            if update.lower() == 'y' :
                name = input("New name: ")
                cursor.execute("UPDATE storage SET product = ? WHERE code = ?", (name, codigo))
                break
            elif update.lower() == 'n' :
                break
            else :
                print('Error! Wrong command\n')
        while True :
            update = input("Do you want to update this item's quantity (y/n): ")
            if update.lower() == 'y' :
                quant = int_input("New quantity: ")
                cursor.execute("UPDATE storage SET quant = ? WHERE code = ?", (quant, codigo))
                break
            elif update.lower() == 'n' :
                break
            else :
                print('Error! Wrong command\n')
        print("Product Updated!\n")
    else :
        print("Product Not Found!\n")

def excluir_produto (codigo) :
    # Exclui um determinado elemento da lista [estoque]
    cursor.execute("SELECT product, code, quant FROM storage WHERE code = ?", (codigo,))
    product = cursor.fetchall()
    if len(product) > 0 : 
        consulta_produto(codigo)
        while True :
            delete = input("Delete this product (y/n): ")
            if delete.lower() == 'y' :
                cursor.execute("DELETE FROM storage WHERE code = ?", (codigo,))
                print('Product Deleted!\n')
                break
            elif delete.lower() == 'n' : 
                print('Aborted!\n')
                break
            else :
                print('Error! Wrong command\n')
    else :
        print("Product Not Found\n")

def exibe_relatorio (sortby) :
    # Exibe um relatório do estoque apresentando o nome, código e quantidade de cada item
    if sortby == 1 :
        sort = "product ASC"
    elif sortby == 2 :
        sort = "product DESC"
    elif sortby == 3:
        sort = "code ASC"
    elif sortby == 4 :
        sort = "code DESC"
    elif sortby == 5 :
        sort = "quant ASC"
    else :
        sort = "quant DESC"
    query = "SELECT product, code, quant FROM storage ORDER BY " + sort
    cursor.execute(query)
    product_list = cursor.fetchall()
    if len(product_list) > 0 :
        header = [description[0] for description in cursor.description]
        print(tabulate(product_list, headers=header, tablefmt="simple_grid"))
    else :
        print("Empty Storage\n")

print('+++++++ MENU – CONTROLE DE ESTOQUE +++++++')
while True :
    # Printa as opções que o usuário possui
    print('1. Cadastrar Produto\n2. Consultar Produto\n3. Atualizar Produto\n4. Excluir Produto\n5. Relatório de Produtos\n6. Encerrar')
    escolha = int_input("Opção escolhida: ")
    print()
    if escolha == 6 : 
        conn.commit()
        conn.close()
        break
    elif escolha == 1 :
        cadastra_produto()
    elif escolha == 2 :
        consulta_produto(insira_codigo())
    elif escolha == 3 :
        atualiza_produto(insira_codigo())
    elif escolha == 4 :
        excluir_produto(insira_codigo())
    elif escolha == 5 :
        sortby = int_input("Sort by:\n1- Product Name Asc\n2- Product Name Desc\n3- Product Code Asc\n4- Product Code Desc\n5- Product Quant Asc\n6- Product Quant Desc\nOption: ")
        exibe_relatorio(sortby)
    else :
        print("Erro! Comando inválido\n") 