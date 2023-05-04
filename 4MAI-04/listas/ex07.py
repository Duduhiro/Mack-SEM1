""" E se sua frase tiver pontuação, como reescrever o programa anterior? Possíveis símbolos a
considerar: ".", ",", ":", ";", "!", "?" """
frase = input('Frase: ')
count = 0
for i in range (len(frase)) :
    if frase[i] == '.' or frase[i] == ',' or frase[i] == ':' or frase[i] == ';' or frase[i] == '!' or frase[i] == '?' or frase[i] == '"' :
        count += 1
        i += 1
    elif frase[i] == ' ' :
        count += 1
print(f"Frases: {count}")
