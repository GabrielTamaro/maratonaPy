num = input().split(" ")

n1 = int(num[0])
n2 = int(num[1])
n3 = int(num[2])

m = (n1 + n2 + abs(n1 - n2)) // 2 #// => pegar o valor inteiro e o abs() => é para pegar o valor absoluto
maior = (n3 + m + abs(n3 - m)) // 2

print(maior, end="")