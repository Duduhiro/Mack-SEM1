""" Escreva um programa em Python que peça para o usuário digite um texto (mensagem: “Digite
um texto: ”) e depois para digitar um número (mensagem: “Digite um número”). Depois, deve
mostrar duas mensagens:1) “A primeira entrada é um dado do tipo <tipo>”; 2) “A segunda
entrada é do tipo <tipo>”, em que <tipo> deve ser trocado pelo tipo dos dados de entrada do
usuário. """
text = input("Insira um texto: ")
n = int(input("Insira um número: "))
print("A primeira entrada é um dado do tipo String, e a segunda entrada é do tipo Int")