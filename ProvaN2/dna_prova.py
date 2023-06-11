sequencia = ['A', 'C', 'G', 'T', 'T', 'C', 'G', 'A']
codem = ['A', 'T', 'C']

def verifica_dna (seq, cod) :
    for i in range (len(seq) - (len(cod) - 1)) :
        if seq[i] == cod[0] :
            for j in range (1, len(cod)) :
                if seq[i + j] != cod[j] :
                    break
            else :
                return i
    else :
        return -1

dna = verifica_dna(sequencia, codem) 
if dna == -1 : 
    print('Codem não encontrado')
else :
    print(f'Codem encontrado na posição: {dna}')