a = int(input("digite o primeiro lado: "))
b = int(input("digite o segundo lado: "))
c = int(input("digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("triangulo equilatero")
    elif a == b or a == c or b == c:
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
else:
    print("não pode formar um triangulo.")