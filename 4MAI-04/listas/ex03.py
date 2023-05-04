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

def cadastra_produto () :
    produto = {
        'name': '',
        'price': 0,
        'quant': 0, 
    }
    produto['name'] = input("Product Name: ")
    while True :
        price = float(input("Price: "))
        if price > 0 : 
            produto['price'] = price
            break
    while True :
        quantity = float(input("Quant: "))
        if quantity > 0 : 
            produto['quant'] = quantity
            break
    print(f'{produto["name"]} sucessfully registered!')
    return produto
     
def remove_produto (nome_remove, lista) :
    for i in range (len(lista)) :
        if lista[i]['name'] == nome_remove :
            lista.pop(i)
            print("Item removed")
            print()
            break
    else :
        print("Error! Name not found")
        print()

def calcula_precos (lista) :
    total = 0
    for i in range (len(lista)) :
        total += (lista[i]['price'] * lista[i]['quant'])
    return total

def exibe_produtos (lista) :
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
        print("Error! Empty list")

print('+++++++++++++++ Armazém da Vila +++++++++++++++')
produtos = []
while True :
    print('1. Cadastrar produto\n2. Remover produto\n3. Calcular valor do estoque\n4. Exibir produtos\n5. Sair')
    seletor = int(input("Type your option: "))
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


