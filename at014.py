print('Conversor de temperatura')

while True:
    grau = float(input('Digite aqui os graus de temperatura: '))
    resposta = input('Essa temperatura está em Celsius, Kelvin ou Fahrenheit? Responda com C, K ou F: ')

    if resposta.lower() == 'c':
        print(f'{grau}°Celsius,')
        cpf = (grau * 9/5) + 32
        cpk = grau + 273.15

        while True:
            pergunta1 = input('deseja converter para qual medida? F ou K: ')

            if pergunta1.lower() == 'f':
                print(f'{grau}°Celsius para Fahrenheit: {cpf}°F.')
                break

            elif pergunta1.lower() == 'k':
                print(f'{grau}°Celsius para Kelvin: {cpk}°K')
                break

            else:
                print('Responda novamente.')


    elif resposta.lower() == 'f':
        print(f'{grau}°Fahrenheit,')
        fpc = (grau - 32) * 5/9
        fpk = (grau - 32) * 5/9 + 273.15

        while True:
            pergunta2 = input('Deseja converter para qual medida? C ou K: ')

            if pergunta2.lower() == 'c':
                print(f'{grau}°Fahrenheit para Celsius: {fpc}°Celsius')
                break

            elif pergunta2.lower() == 'k':
                print(f'{grau}°Fahrenheit para Kelvin: {fpk:.3f}°Kelvin')
                break

            else:
                print('Erro, Digite sua resposta novamente')

    elif resposta.lower() == 'k':
        print(f'{grau}°Kelvin')
        kpc = grau - 273.15
        kpf = grau - (273.15) * 9/5 + 32

        while True:
            pergunta3 = input('Deseja converter para qual medida? C ou F: ')

            if pergunta3.lower() == 'c':
                print(f'{grau}°Kelvin para Celsius: {kpc:.2f}°Celsius.')
                break

            elif pergunta3.lower() == 'f':
                print(f'{grau}°Kelvin para Fahrenheit: {kpf:.2f}°Fahrenheit.')
                break

            else:
                print('Erro, Digite sua resposta novamente')
        break
    else:
        print('Inválido, responda novamente')

    print('Cabô')



