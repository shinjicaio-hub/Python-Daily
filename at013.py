print('Reajuste Salarial')
sal = float(input('Digite o salário que deseja reajustar: R$'))
dez = sal - (sal * (10/100))
percent = int(input(f'Quantos % deseja ajustar?\nExemplos:\n10% = R${sal * (10/100):.2f})'))

while True:
 resposta = input('Deseja diminuir ou aumentar o Salário selecionado? (Responda com - ou +): ')

 if resposta == '-':
    print(f'O salário com o reajuste de {percent}% (-{sal * (percent/100):.1f}) ficará no valor de: R${sal - (sal * (percent/100)):.2f}')
    break
 elif resposta == '+':
    print(f'O salário com o reajuste de {percent}% (+{sal * (percent/100):.1f}) ficará no valor de: R${sal + (sal * (percent/100)):.2f}')
    break
 else:
    print('Se quiser sim mano, responda direito.')
