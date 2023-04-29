# Elabore um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"

# O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
# responder Sim a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
# "Assassino". Caso contrário, ela será classificada como "Inocente".

print("---------------Programa de reconhecimento de culpabilidade---------------")
print("\nPara responder, use 1 para sim e 0 para não")
result = 0
q1 = input("Telefonou para a vítima? ").lower()
if q1 == "sim" :
    result += 1
q2 = input("Esteve no local do crime? ").lower()
if q2 == "sim" :
    result += 1
q3 = input("Mora perto da vítima? ").lower()
if q3 == "sim" :
    result += 1
q4 = input("Devia para a vítima? ").lower()
if q4 == "sim" :
    result += 1
q5 = input("Já trabalhou com a vítima? ").lower()
if q5 == "sim" :
    result += 1

if result == 2 :
    print("Você está sendo considerado como suspeito e deve permanecer na delegacia")
elif result == 3 or result == 4 :
    print("Você está sendo considerado como cúmplice e pode delatar o seu companheiro para uma pena mais branda")
elif result == 5 :
    print("ASSASSINO!!!!!")
else :
    print("Você está sendo considerado inocente e está liberado para ir embora")