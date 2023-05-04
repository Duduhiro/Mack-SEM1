"""  Tanto cadeias DNA quanto RNA são sequências de nucleotídeos. O DNA é formado por:
adenina (A), citosina (C), guanina (G) e timina (T); enquanto o RNA é formado por: adenina (A),
citosina (C), guanina (G) e uracila (U). Dada uma cadeia qualquer de DNA, a transcrição em RNA
é dada formado substituindo cada nucleotídeo pelo seu complemento. Isto é: G por C; C por
G; T por A e A por U.
Implemente uma função que receba como parâmetro uma cadeia de DNA dada na forma de
string, e retorne o RNA complementar. Considere como inválido se um nucleotídeo não for A,
C, G ou T. """

def dna_to_rna (dna) :
    rna = ''
    for i in range (len(dna)) :
        if dna[i].upper() == 'A' :
            rna += 'U'
        elif dna[i].upper() == 'G' :
            rna += 'C' 
        elif dna[i].upper() == 'C' :
            rna += 'G'
        elif dna[i].upper() == 'T' :
            rna += 'A'
        else :
            break
    else :
        return rna
    return "Error! DNA Invalid"

dna = input("DNA: ")
print(dna_to_rna(dna))