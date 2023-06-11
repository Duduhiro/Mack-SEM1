""" 7) Calcule e apresente o volume de uma lata de óleo, que é dada por: 𝑣 = 𝜋 ∙ 𝑟2 ∙ 𝑎𝑙𝑡𝑢𝑟� """

raio = int(input("Raio da lata: "))
altura = int(input("Altura da lata: "))

volume = 3.14159 * (raio * raio) * altura

print(f'O volume da lata é de: {volume:.2f} U.M.')