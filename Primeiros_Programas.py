N = int(input())
casas = []
for i in range(N):
    casas.append(int(input()))
K = int(input())

metade = N/2
v = int(metade) - 1
metade = int(metade) - 1
while v < N:
    i = 0
    while i < metade:
        if casas[i] + casas[v] == K:
            print(f"{casas[i]} {casas[v]}")
            break
    v = v + 1