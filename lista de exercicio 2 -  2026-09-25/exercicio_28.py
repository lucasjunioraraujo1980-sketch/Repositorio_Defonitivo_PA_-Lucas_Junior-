numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\nLista principal:", numeros)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)
