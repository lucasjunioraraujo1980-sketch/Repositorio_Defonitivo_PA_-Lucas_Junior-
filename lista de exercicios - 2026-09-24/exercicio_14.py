n1 = int(input("digite a primero numero: "))
n2 = int(input("digite o segundo numero: "))

o = int(input("1 - soma; 2 - subtração; 3 - multiplicação; 4 - divisão; digite qualquer numero para fechar: "))

if o == 1:
    print(f"{n1 + n2}")
elif o == 2:
    print(f"{n1 - n2}")
elif o == 3:
    print(f"{n1 * n2}")
elif o == 4:
    print(f"{n1 / n2 }")
else:
    print("programa finalizado ")