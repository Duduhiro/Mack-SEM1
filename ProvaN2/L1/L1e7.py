""" 7) Escreva um programa em Python que peça para o usuário digite um texto (mensagem: “Digite 
um texto: ”) e depois para digitar um número (mensagem: “Digite um número”). Depois, deve 
mostrar duas mensagens:1) “A primeira entrada é um dado do tipo <tipo>”; 2) “A segunda 
entrada é do tipo <tipo>”, em que <tipo> deve ser trocado pelo tipo dos dados de entrada do 
usuário. """

text = input("Texto: ")
num = int(input("Número: "))

print(f'Data type 1 {type(text)} | Data type 2 {type(num)}')