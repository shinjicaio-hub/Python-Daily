import math
cat_adj = float(input('comprimento do cateto adjacente: '))
cat_opo = float(input('comprimento do cateto oposto: '))
hip_quad = cat_adj**2 + cat_opo**2
hipo = round(math.sqrt(hip_quad), 2)

print(f'Com o cateto oposto de valor: {cat_opo}, e cateto adjacente: {cat_adj}, O valor da hipotenusa é: {hipo}.')
print(hipo)