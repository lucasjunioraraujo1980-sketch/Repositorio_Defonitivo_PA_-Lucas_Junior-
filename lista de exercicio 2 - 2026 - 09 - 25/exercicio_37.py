produtos = []
quantidades = []

while True:
    print("\n--- ESTOQUE ---")
    print("1 - Adicionar Produto")
    print("2 - Dar Baixa")
    print("3 - Ver Estoque")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))

        produtos.append(nome)
        quantidades.append(quantidade)

        print("Produto adicionado!")

    elif opcao == 2:

        nome = input("Digite o produto que deseja retirar: ")

        if nome in produtos:
            posicao = produtos.index(nome)

            quantidade = int(input("Digite a quantidade para retirar: "))

            if quantidade <= quantidades[posicao]:
                quantidades[posicao] -= quantidade
                print("Baixa realizada!")
            else:
                print("Estoque insuficiente!")

        else:
            print("Produto não encontrado!")

    elif opcao == 3:

        print("\n--- ESTOQUE ATUAL ---")

        for i in range(len(produtos)):
            print(produtos[i], "-", quantidades[i])

    elif opcao == 4:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
