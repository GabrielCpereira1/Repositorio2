def busca_forca_bruta(v, alvo):  
    for i in range(len(v)):
        if v[i] == alvo:
           return i + 1


    return -1

v = [1, 3, 5, 10, 15, 19, 89]
alvo = 3
print("O alvo está na posição:", busca_forca_bruta(v, alvo))
