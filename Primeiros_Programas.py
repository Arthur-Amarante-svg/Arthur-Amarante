N = int(input())
casas = []
for i in range(N):
    casas.append(int(input()))
K = int(input())
for i in range(len(casas)):
    aux = len(casas) - i
    v = i + 1
    while v < len(casas):
        if casas[i] + casas[v] == K:
            print(f"{casas[i]} {casas[v]}")
        v = v + 1