def mdc(L, A):
    if A == 0:
        return L
    else:
        return mdc(A, L % A)

print(mdc(168, 64))
print(mdc(24, 16))