frase = input("Digite uma frase: ")

quantidade_a = 0
quantidade_palavras = 0
dentro_palavra = False

for letra in frase:

    if letra == "a" or letra == "A":
        quantidade_a += 1

    if letra != " " and dentro_palavra == False:
        quantidade_palavras += 1
        dentro_palavra = True

    elif letra == " ":
        dentro_palavra = False

print("\nQuantidade de palavras:", quantidade_palavras)
print("Quantidade de letras A:", quantidade_a)
