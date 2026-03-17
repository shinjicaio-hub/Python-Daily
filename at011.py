import math
print('Podemos dizer quanto de tinta voçê precisa!')
a = float(input('Qual a altura de sua parede? '))
l = float(input('Qual a largura de sua parede? '))
area = (l * a)
# 1l de tinta pinta 9m² de parede
tinta = math.ceil(area/9)
preco = float(tinta * 8)
print(f'A sua parede de {a}m e {l}m de largura, precisará de {tinta:.1f}l de tinta.')
print(f'O preço de {tinta:.1f}l de tinta ficaria em: R${preco:.2f}.')

if tinta >= 12:
    print('Temos disponível a partir de 12 Litros, seguindo com 18l, 25l, 30, e 40l. Escolha a melhor para pintar sua parede!')

else:
    print('Nossos produtos são de no mínimo 12 litros, se for de sua preferência uma lata com menor quantidade, recomendo visitar em nosso site de tintas para Pequenas Reformas')

