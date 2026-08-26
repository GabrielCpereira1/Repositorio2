import random
figurinhas = set()
pacotinhos = 0
repetida = 0
while len(figurinhas) < 50:

    for i in range(5):
        figurinha = random.randint(1, 50)

        if figurinha in figurinhas:
            repetida = repetida + 1
        else:
            figurinhas.add(figurinha)

    pacotinhos = pacotinhos + 1

print("Número de pacotinhos abertos:", pacotinhos)
print("Número de figurinhas repetidas:", repetida)
print("Figurinhas obtidas:", sorted(figurinhas))
print("Número de figurinhas obtidas:", len(figurinhas))
