linhas = int(input())

total = []
for i in range(0, linhas):
    num = list(map(int, input().split(";")))
    somar = sum(num)
    total.append(somar)

print(*total, sep='\n', end="")
