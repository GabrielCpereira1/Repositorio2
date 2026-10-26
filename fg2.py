def quick_sort(v):
    maiores = []
    menores = []

    if len(v) <= 1:
        return v

    pivo = v[-1]

    for i in v[:-1]:
        if i < pivo:
            menores.append(i)
        elif i > pivo:
            maiores.append(i)
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

v = [8, 7, 9, -1, 19,5, 3, 2, 1, 0,30]
print(quick_sort(v))