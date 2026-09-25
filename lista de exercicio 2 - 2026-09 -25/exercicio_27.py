numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("\nNúmeros pares:")

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
