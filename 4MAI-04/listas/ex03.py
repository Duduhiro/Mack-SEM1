""" Faça um programa que monte o menu abaixo, utilize lista para o cadastro dos produtos e
implemente as funções listadas:
+++++++++++++++ Armazém da Vila +++++++++++++++
1. Cadastrar produto
2. Remover produto
3. Calcular valor do estoque
4. Exibir produtos
5. Sair
Digite sua opção:
Observações sobre as operações:
▪ A op. 1 insere em uma lista o nome do produto, quantidade e valor
▪ A op. 2 solicita o nome do produto e o remove da lista
▪ A op. 3 calcula o valor em R$ do total de produtos cadastrados no sistema
▪ A op. 4 mostra os produtos cadastrados e a quantidade em estoque
Cada operação deve ser implementada como uma função. """

def cadastra_produto () : # Função para cadastrar um produto
    produto = { # Dicionário produto com as categorias nome, preço unitário e quantidade
        'name': '',
        'price': 0,
        'quant': 0, 
    }
    produto['name'] = input("Product Name: ") # Insere o nome do produto na categoria nome
    while True :
        # Insere o preço caso ele for maior que zero
        price = float(input("Price: "))
        if price > 0 : 
            produto['price'] = price
            break
    while True :
        # Insere a quantidade caso ela for maior que zero
        quantity = float(input("Quant: "))
        if quantity > 0 : 
            produto['quant'] = quantity
            break
    print(f'{produto["name"]} sucessfully registered!') # Printa operação sucedida
    return produto # Retorna o dicionário

def remove_produto (nome_remove, lista) : # Função para remover um produto da lista de produtos
    for i in range (len(lista)) : # Itera entre os itens da lista produtos até achar um item que possua o nome correspondente ao que vai ser deletado
        if lista[i]['name'] == nome_remove :
            lista.pop(i) # Remove da lista o item que possui o mesmo nome que foi inserido como parâmetro da função
            print("Item removed")
            print()
            break
    else :
        # Caso não haja um nome correspondente, lança uma mensagem de erro 
        print("Error! Name not found")
        print()

def calcula_precos (lista) :
    # Calcula o preço total dos itens da lista
    total = 0
    for i in range (len(lista)) :
        total += (lista[i]['price'] * lista[i]['quant'])
    return total

def exibe_produtos (lista) :
    # Printa todos os produtos da lista, seguido por seus respectivos preços e quantidades
    if len(lista) != 0 :
        print("Product     |Quant| R$")
        for i in range (len(lista)) :
            spaces = 12 - len(lista[i]['name'])
            print(lista[i]['name'], end='')
            print(' ' * spaces, end='| ')
            print(f"{lista[i]['quant']:4.0f}|", end='')
            print(f"{lista[i]['price'] * lista[i]['quant']:.2f} ({lista[i]['price']:.2f}) ")
        print(f'Total             |{calcula_precos(lista):.2f}')
    else :
        # Caso a lista de produtos esteja vazia, lança uma mensagem de erro
        print("Error! Empty list")

print('+++++++++++++++ Armazém da Vila +++++++++++++++')
produtos = [] # Inicia a lista produtos | Cada elemento da lista será um dicionário produto que irá possuir 3 características (nome, quant e preço)
while True :
    print('1. Cadastrar produto\n2. Remover produto\n3. Calcular valor do estoque\n4. Exibir produtos\n5. Sair')
    seletor = int(input("Type your option: "))
    # Seletor para o usuário escolher entre 1- cadastrar um item | 2- remover um item
    # 3- calcular preço total da lista | 4- exibir os produtos | 5- sair
    print()
    if seletor == 5 :
        break
    elif seletor == 1 :
        produtos.append(cadastra_produto())
        print()
    elif seletor == 2 :
        remover = input("Item to remove: ")
        remove_produto(remover, produtos)
    elif seletor == 3 :
        print(f"Total in storage: R${calcula_precos(produtos):.2f}")
        print()
    elif seletor == 4 :
        exibe_produtos(produtos)
        print()
    else :
        print("Error! Wrong command")


