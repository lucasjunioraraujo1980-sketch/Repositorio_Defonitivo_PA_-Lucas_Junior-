numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("\nPosições e valores:")

for i in range(5):
    print("Posição:", i, "| Valor:", numeros[i])
