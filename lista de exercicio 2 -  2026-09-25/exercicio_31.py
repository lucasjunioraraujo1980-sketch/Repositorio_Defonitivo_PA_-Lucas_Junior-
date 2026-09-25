numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("\nOrdem digitada:")

for i in range(5):
    print(numeros[i])

print("\nOrdem inversa:")

for i in range(4, -1, -1):
    print(numeros[i])
