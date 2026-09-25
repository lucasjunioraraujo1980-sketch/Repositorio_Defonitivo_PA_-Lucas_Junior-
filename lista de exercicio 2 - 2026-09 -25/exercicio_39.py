poltronas = [False] * 10

while True:

    print("\n--- POLTRONAS ---")

    for i in range(10):
        if poltronas[i] == False:
            print(i, "- Livre")
        else:
            print(i, "- Ocupada")

    numero = int(input("\nDigite o número da poltrona (-1 para sair): "))

    if numero < 0:
        print("Programa encerrado.")
        break

    if numero > 9:
        print("Poltrona inválida!")

    elif poltronas[numero] == True:
        print("Ocupada!")

    else:
        poltronas[numero] = True
        print("Reservada!")
