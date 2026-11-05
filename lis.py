sequencia = [10, 22, 9, 33, 21, 50, 41, 60]

dp = [1] * len(sequencia)

for i in range(1, len(sequencia)):
    for j in range(i):
        if sequencia[i] > sequencia[j]:
            dp[i] = max(dp[i], dp[j] + 1)

resultado = max(dp)

print("Maior subsequência crescente:", resultado)
