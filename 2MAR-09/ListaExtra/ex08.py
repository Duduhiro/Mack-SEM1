# Escreva um programa em Python para calcular em qual dia da semana
# caiu uma data qualquer. Para isso, leia três valores inteiros
# correspondentes a dia, mês e ano; e então compute o resultado para
# a fórmula:
# 𝐷𝑖𝑎𝑆𝑒𝑚𝑎𝑛𝑎 = (𝑎𝑛𝑜 − 1901) × 365 + (𝑎𝑛𝑜 − 1901) ÷ 4 + 𝑑𝑖𝑎
# + (𝑚𝑒𝑠 − 1) × 31
# − [(𝑚𝑒𝑠 × 4 + 23) ÷ 10] × [(𝑚𝑒𝑠 + 12) ÷ 15]
# + [(4 − 𝑎𝑛𝑜 𝑚𝑜𝑑 4) ÷ 4) × [(𝑚𝑒𝑠 + 12) ÷ 15]
# O resultado determina o dia da semana, que deve ser interpretado
# segundo a tabela ao lado.

dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))

diaSemana = int((ano - 1901) * 365 + (ano - 1901) / 4 + dia + (mes - 1) * 31 - ((mes * 4 + 23) / 10) * ((mes + 12) / 15) + ((4 - ano) / 4) * ((mes + 12) / 15))

if diaSemana == 0 :
    print("Segunda-Feira")
elif diaSemana == 1 :
    print("Terça-Feira")
elif diaSemana == 2 :
    print("Quarta-Feira")
elif diaSemana == 3 :
    print("Quinta-Feira")
elif diaSemana == 4 :
    print("Sexta-Feira")
elif diaSemana == 5 :
    print("Sábado")
else : 
    print("Domingo")