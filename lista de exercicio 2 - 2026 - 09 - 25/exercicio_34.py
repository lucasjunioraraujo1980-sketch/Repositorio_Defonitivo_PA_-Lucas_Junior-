votos = [0, 0, 0, 0, 0]

while True:
    print("\n--- URNA ---")
    print("1 - João")
    print("2 - Maria")
    print("3 - José")
    print("4 - Nulo")
    print("5 - Branco")
    print("0 - Encerrar")

    voto = int(input("Digite seu voto: "))

    if voto == 0:
        break

    if voto >= 1 and voto <= 5:
        votos[voto - 1] += 1
        print("Voto registrado!")
    else:
        print("Voto inválido!")

print("\n--- RESULTADO ---")
print("João:", votos[0])
print("Maria:", votos[1])
print("José:", votos[2])
print("Nulos:", votos[3])
print("Brancos:", votos[4])

maior = max(votos[0], votos[1], votos[2])

if maior == votos[0] and maior != votos[1] and maior != votos[2]:
    print("Vencedor: João")
elif maior == votos[1] and maior != votos[0] and maior != votos[2]:
    print("Vencedor: Maria")
elif maior == votos[2] and maior != votos[0] and maior != votos[1]:
    print("Vencedor: José")
else:
    print("Houve empate entre os candidatos.")
