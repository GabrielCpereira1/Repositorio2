notas = []
for i in range(4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
