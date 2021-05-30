linhas = int(input())

raios = []
for i in range(0, linhas):
    raios.append(input())

for r in range(0, len(raios)):
    raio = list(map(int, raios[r].split()))
    if raio[0] + raio[1] <= raio[2]:
        print("CABE!", end="" if r == len(raios) - 1 else "\n")
    else:
        print("NAO CABE!", end="" if r == len(raios) - 1 else "\n")