print('-='*20)
print('ANALISADOR DE TRIÂNGULO')
print('-='*20)
r1 = float(input('Primeiro lado:'))
r2 = float(input('Segundo lado:'))
r3 = float(input('Terceiro lado:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('esses valoes formam um triangulo!')
    if r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é ESCALENO!')
    else:
        print('Esse triângulo é ISÓSCELES')
else:
    print('Esses valores não formam um triangulo!')
print('-='*20)
print('FIM DO PROGRAMA')
print('-='*20)
