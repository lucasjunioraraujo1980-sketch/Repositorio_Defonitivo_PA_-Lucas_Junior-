nome = ""
conta = ""
saldo = 0
criada = False

while True:

    print("\n--- BANCO ---")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato / Ver Saldo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        if criada == True:
            print("A conta já foi criada!")

        else:
            nome = input("Digite o nome: ")
            conta = input("Digite o número da conta: ")
            saldo = 0
            criada = True

            print("Conta criada com sucesso!")

    elif opcao == 2:

        if criada == False:
            print("Crie uma conta primeiro!")

        else:
            valor = float(input("Digite o valor do depósito: "))

            if valor > 0:
                saldo += valor
                print("Depósito realizado!")
            else:
                print("Valor inválido!")

    elif opcao == 3:

        if criada == False:
            print("Crie uma conta primeiro!")

        else:
            valor = float(input("Digite o valor do saque: "))

            if valor <= 0:
                print("Valor inválido!")

            elif valor > saldo:
                print("Saldo insuficiente!")

            else:
                saldo -= valor
                print("Saque realizado!")

    elif opcao == 4:

        if criada == False:
            print("Crie uma conta primeiro!")

        else:
            print("\n--- EXTRATO ---")
            print("Nome:", nome)
            print("Conta:", conta)
            print("Saldo: R$", saldo)

    elif opcao == 5:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
