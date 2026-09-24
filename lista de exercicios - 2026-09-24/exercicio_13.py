n1 = float(input("digite a primero nota: "))
n2 = float(input("digite a segundo nota: "))

m = round((n2 + n1) / 2)

if m >= 7:
    print("você foi aprovado")
elif m >= 5 and m <= 6.9:
    print("voce esta de recuparação")
else:
    print("voce foi reprovado")