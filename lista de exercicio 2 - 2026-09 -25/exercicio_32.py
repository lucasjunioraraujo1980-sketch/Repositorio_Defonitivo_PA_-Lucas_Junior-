notas = []
soma = 0

for i in range(5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    soma += nota

media = soma / 5

print("\nMédia da turma:", media)

quantidade = 0

for nota in notas:
    if nota > media:
        quantidade += 1

print("Alunos acima da média:", quantidade)
