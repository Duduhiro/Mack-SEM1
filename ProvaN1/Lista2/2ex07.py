""" Calcule e apresente o volume de uma lata de óleo, que é dada por: v = 𝜋 ∙ r2 ∙ altura """
import math

altura = int(input("Altura da lata: "))
raio = int(input("Raio da lata: "))
volume = math.pi * math.pow(raio, 2) * altura
print(f"O volume da lata é {volume:.2f}")