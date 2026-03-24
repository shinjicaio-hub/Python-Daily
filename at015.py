print('Contador de Aluguel de carro')
dia = float(input('Quantos dias completos com o carro alugado? '))
km = float(input('Quantos Km rodados? '))

contdia = dia * 60

contkm  = km * 0.15

total = contkm + contdia

print(f'O valor total do aluguel é de R${total:.2f}.')



