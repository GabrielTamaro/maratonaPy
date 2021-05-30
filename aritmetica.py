x = int(input())
s1 = input()
y = int(input())
s2 = input()
z = int(input())

calcular = str(x) + s1 + str(y) + s2 + str(z)

mult = calcular.find('*')
div = calcular.find('/')

if mult < 0 and div < 0:
    if s1 == '+' and s2 == '-':
        resultado = x + y - z
    elif s1 == '+' and s2 == '+':
        resultado = x + y + z
    elif s1 == '-' and s2 == '+':
        resultado = x - y + z
    else:
        resultado = x - y - z
elif mult > 0 and div > 0:
    if x == 0 or y == 0 or z == 0:
        resultado = 'erro'
    elif mult > div:
        resultado = int(x / y * z)
    else:
        resultado = int(x * y / z)
else:
    if mult > 0 and div < 0:
        if mult == 3:
            if s1 == '+':
                resultado = x + y * z
            else:
                resultado = x - y * z
        else:
            if s2 == '+':
                resultado = x * y + z
            else:
                resultado = x * y - z
    else:
        if x == 0 or y == 0 or z == 0:
            resultado = 'erro'
        elif div == 3:
            if s1 == '+':
                resultado = int(x + y / z)
            else:
                resultado = int(x - y / z)
        else:
            if s2 == '+':
                resultado = int(x / y + z)
            else:
                resultado = int(x / y - z)

print(resultado, end='')