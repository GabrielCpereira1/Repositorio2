def pesar(grupo1, grupo2):
    # Simula uma balança.
    # Para este exemplo, a moeda falsa é a número 7.
    moeda_falsa = 7

    peso1 = sum(1 for moeda in grupo1 if moeda != moeda_falsa)
    peso2 = sum(1 for moeda in grupo2 if moeda != moeda_falsa)

    # Cada moeda verdadeira tem peso 1.
    # A moeda falsa tem peso 0.5.
    peso1 = sum(0.5 if moeda == moeda_falsa else 1 for moeda in grupo1)
    peso2 = sum(0.5 if moeda == moeda_falsa else 1 for moeda in grupo2)

    if peso1 < peso2:
        return -1
    elif peso2 < peso1:
        return 1
    else:
        return 0


def encontrar_falsa(moedas):
    # Divide as moedas em três grupos
    grupo1 = moedas[:3]
    grupo2 = moedas[3:6]
    grupo3 = moedas[6:9]

    # Primeira pesagem
    resultado = pesar(grupo1, grupo2)

    if resultado == -1:
        suspeitas = grupo1
    elif resultado == 1:
        suspeitas = grupo2
    else:
        suspeitas = grupo3

    # Segunda pesagem: compara duas moedas suspeitas
    resultado = pesar([suspeitas[0]], [suspeitas[1]])

    if resultado == -1:
        return suspeitas[0]
    elif resultado == 1:
        return suspeitas[1]
    else:
        return suspeitas[2]


moedas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

falsa = encontrar_falsa(moedas)

print("Moeda falsa:", falsa)
print("Número de pesagens: 2")