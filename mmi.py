linhas = int(input())

notas = []
for i in range(0, linhas):
    notas.append(input())

for n in range(0, len(notas)):
    nota = list(map(int, notas[n].split()))
    print(min(nota), end=" ")
    print(max(nota))
    if len(set(nota)) == 1:
        print("S", end="" if n == len(notas) - 1 else "\n")
    else:
        print("N", end="" if n == len(notas) - 1 else "\n")
    