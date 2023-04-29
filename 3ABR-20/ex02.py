""" Defina uma função em Python chamada CelsiusToFahrenheit, capaz de receber uma medida de
temperatura em graus Celsius como parâmetro, calcular o valor correspondente em graus
Fahrenheit e retorná-lo. Lembre-se que a fórmula para conversão entre medias é: 𝐹 = 9/5 𝐶 + 32 """

def celsius_to_fahrenheit (celsius) :
    fahrenheit = 9 / 5 * celsius + 32
    return fahrenheit
celsius = int(input("Celsius: "))
print(f"Fahrenheit: {celsius_to_fahrenheit(celsius)}")