""" Faça um programa que leia um número indeterminado de notas e armazene os valores em
uma lista. A entrada das notas é encerrada quando for digitado -1. Após esta entrada de dados,
faça o seguinte:
▪ Mostre a quantidade de notas que foram lidas.
▪ Exiba todas as notas na ordem em que foram informadas, uma abaixo do outra.
▪ Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
▪ Calcule e mostre a soma das notas.
▪ Calcule e mostre a média das notas.
▪ Calcule e mostre a quantidade de notas acima da média calculada. """

notas = []
while True :
    nota = float(input("Grade (-1 to exit): "))
    if nota == -1 :
        break
    elif nota >= 0 and nota <= 10 :
        notas.append(nota)
    else :
        print("Error! Grade invalid")
print(f"Foram lidas {len(notas)} notas")
print(f"Notas na ordem que foram registradas\n{notas}\n")
print(f"Notas na ordem inversa que foram registradas\n{notas[::-1]}\n")
print(f"Soma das notas: {sum(notas):.2f}")
media = sum(notas) / len(notas)
acima = 0
for i in range (len(notas)) :
    if notas [i] >= media :
        acima += 1
print(f"A média foi {media:.2f} e {acima} alunos ficaram acima dela")