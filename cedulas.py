valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]

cont = 0
while cont != len(notas):
    troco = valor // notas[cont]
    valor -= troco * notas[cont]
    print(f'{troco} nota(s) de R$ {notas[cont]}', end="" if cont == len(notas) - 1 else '\n')
    cont += 1
