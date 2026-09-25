alunos = int(input("Quantos alunos existem? "))

notas = []

for i in range(alunos):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Média da turma:", media)