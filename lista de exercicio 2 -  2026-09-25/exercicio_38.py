import random

campo = [0] * 10

# Coloca 3 minas em posições diferentes
minas = random.sample(range(10), 3)

for posicao in minas:
    campo[posicao] = 1

print("Jogo iniciado!")
print("Escolha posições de 0 a 9.")

perdeu = False

for i in range(5):

    posicao = int(input("Escolha uma posição: "))

    if posicao < 0 or posicao > 9:
        print("Posição inválida!")
        continue

    if campo[posicao] == 1:
        print("💥 Você pisou em uma mina!")
        print("Você perdeu!")
        perdeu = True
        break
    else:
        print("Posição segura!")

if perdeu == False:
    print("\nParabéns! Você sobreviveu aos 5 passos!")
