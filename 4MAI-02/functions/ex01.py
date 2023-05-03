def valorPagamento (prest, atraso) :
    if atraso == 0 :
        return prest
    else :
        multa = prest * 1.03
        juros = prest * (atraso * 0.001)
        prest = multa + juros
    return prest

def main():
    valor = float(input())
    dias = int(input())
    print(valorPagamento(valor,dias))
main()