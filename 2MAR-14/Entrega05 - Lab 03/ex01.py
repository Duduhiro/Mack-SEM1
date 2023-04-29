tipo = input("")
q = int(input(""))

if tipo == "D" and q <= 50 :
    result = q * 200.00
elif tipo == "D" and q > 50 :
    result = q * 120.00
elif tipo == "N" and q <= 50 :
    result = q * 100.00
elif tipo == "N" and q > 50 :
    result = q * 80.00
print("%.2f" %(result))