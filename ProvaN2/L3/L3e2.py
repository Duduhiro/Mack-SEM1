""" A tributação de impostos aplica alíquotas diferentes para os produtos, de acordo com a
sua natureza fabril. Implemente um programa que leia o código de
um determinado produto e mostre a sua classificação categórica do fisco, segundo a
tabela dada a seguir: """

codigo = int(input("Insira o código: "))

if codigo == 1 :
    print("Alimento não-perecível")
elif codigo == 2 or codigo == 3 or codigo == 4 : 
    print("Alimento perecível")
elif codigo == 5 or codigo == 6 :
    print("Vestuário")
elif codigo == 7 :
    print("Higiene pessoal")
elif codigo == 8 or codigo == 9 or codigo == 10 :
    print("Utensílios domésticos")
else : 
    print("Categoria inválida")