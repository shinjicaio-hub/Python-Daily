import math
ang = input('Digite o valor do Ângulo: ')


try:
    ang_float = float(ang)
    if ang_float % 1 == 0:
        ang_int = int(ang_float)
        print(f'Você digitou o ângulo: {ang_int}')
        senoint = round(math.sin(ang_int), 2)
        cosint  = round(math.cos(ang_int), 2)
        tangint = round(math.tan(ang_int), 2)

        print(f'seno: {senoint:.f}; Cosseno: {cosint}; Tangente: {tangint}.')

    else:
        print(f'Você digitou o ângulo: {ang_float}')
        senofloat = round(math.sin(ang_float), 2)
        cosfloat  = round(math.cos(ang_float), 2)
        tangfloat = round(math.tan(ang_float), 2)
        print(f'Seno: {senofloat}; Cosseno: {cosfloat}; Tangente: {tangfloat}.')



except ValueError as ve:
    print(f'{ve}')

print('Código finalizado.')



