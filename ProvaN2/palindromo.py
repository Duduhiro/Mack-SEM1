""" Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita de forma normal 
(esquerda para a direita) ou inversa (direita para a esquerda). Por exemplo: as palavras OSSO 
e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
Assim, a frase “SUBI NO ONIBUS” é o exemplo de uma frase palíndromo. Faça um programa 
que leia uma palavra ou frase, mostrando−a na tela e dizendo se é ou não um palíndromo """

text = input("Text: ")
text = text.replace(" ", "")
inverted = text [::-1]

for i in range(len(text)) :
    if text[i].lower() != inverted[i].lower() :
        print('Não é palindromo')
        break
else :
    print('É palindromo')