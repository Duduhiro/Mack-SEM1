""" Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita de forma normal
(esquerda para a direita) ou inversa (direita para a esquerda). Por exemplo: as palavras OSSO
e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
Assim, a frase “SUBI NO ONIBUS” é o exemplo de uma frase palíndromo. Faça um programa
que leia uma palavra ou frase, mostrando−a na tela e dizendo se é ou não um palíndromo. """

frase = input("Frase: ")
frase.replace(' ', '')
inverso = frase[::-1]

for i in range (int(len(frase) / 2)) :
    if frase[i] != inverso[i] :
        break
else :
    print("É palindromo")