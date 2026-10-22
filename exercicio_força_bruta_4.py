dna = "ACGTACGTTACGGAATCG"
procurada = "TACG"
encontrada = False

for i in range(len(dna)):
    trecho = dna[i:i + len(procurada)]

    if trecho == procurada:
        encontrada = True
        print("Sequência encontrada na posição", i + 1)

if not encontrada:
    print("Sequência não foi encontrada.")

