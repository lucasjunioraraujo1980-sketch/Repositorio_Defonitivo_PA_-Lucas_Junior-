i = int(input("digite sua idade: "))

if i < 16:
    print("menores de 16 não votam.")
elif i >= 16 and i <= 17:
    print("seu voto é facultativo")
elif i >= 65:
    print("seu voto é facultativo")
else:
    print("seu voto é obrigatorio")