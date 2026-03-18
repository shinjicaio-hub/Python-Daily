print('Calculador de Desconto.')
produt = float(input('Digite o valor do produto: R$'))
desc = float(input('Digite agora o Valor do desconto (%): '))

valdesc = produt * (desc/100)
vafinal = produt - valdesc
print(f'O seu produto de valor:R${produt:.2f}, ficará por R${vafinal:.2f}!')
print(f'Com o desconto de {desc:.1f}%, você economizará R${valdesc:.2f}!')