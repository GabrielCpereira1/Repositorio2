import random
numeros = random.randint(1, 60)
numeros = set()
while len(numeros) < 6:
    numeros.add(random.randint(1, 60))
print("Números da loteria:", sorted(numeros))