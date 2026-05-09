N = int(input())
resultados = []
teste = 1
while N > 0:
    pontoA = 0
    pontoB = 0
    for i in range(N):
        A, B = map(int, input().split())
        if A < B:
            pontoB = pontoB + 1
        else:
            pontoA = pontoA + 1
    if pontoA < pontoB:
        resultados.append("Beto")
    else:
        resultados.append("Aldo")
    N = int(input())
for resultado in resultados:
    print(f"Teste {teste}")
    print(resultado)
    print()
    teste = teste + 1