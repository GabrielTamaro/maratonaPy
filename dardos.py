alvo = input().split(" ")

x = int(alvo[0])
y = int(alvo[1])

if x > 0 and y > 0:
    print("R1", end="")
elif x < 0 and y > 0:
    print("R2", end="")
elif x < 0 and y < 0:
    print("R3", end="")
elif x > 0 and y < 0:
    print("R4", end="")
elif x == 0 and y == 0:
    print("NO ALVO!", end="")