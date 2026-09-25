numeros = []

for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

busca = int(input("Digite o número que deseja procurar: "))

encontrou = False

for i in range(8):
    if numeros[i] == busca:
        print("Número encontrado na posição", i)
        encontrou = True

if encontrou == False:
    print("Número não encontrado.")
