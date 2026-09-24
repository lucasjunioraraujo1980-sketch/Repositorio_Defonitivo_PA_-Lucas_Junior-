a = int(input("digite o ano: "))

if a % 400 == 0:
    print("é bissexto")
elif a % 100 == 0:
    print("não é bissexto")
elif a % 4 == 0:
    print("é bissexto")
else:
    print("não é bissexto")