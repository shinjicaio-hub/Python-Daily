n = int(input('Digite o número para ver sua tabuada: '))

tab1  = n * 1
tab2  = n * 2
tab3  = n * 3
tab4  = n * 4
tab5  = n * 5
tab6  = n * 6
tab7  = n * 7
tab8  = n * 8
tab9  = n * 9
tab10 = n * 10

# print(f'A tabuada de {n} é:\n{n} x 1 = {tab1}\n{n} x 2 = {tab2}\n{n} x 3 = {tab3}\n{n} x 4 = {tab4}\n{n} x 5 = {tab5}\n{n} x 6 = {tab6}\n{n} x 7 = {tab7}\n{n} x 8 = {tab8}\n{n} x 9 = {tab9}\n{n} x 10 = {tab10}')

(print
 (f'''
 TABUADA
{n} * {1} = {tab1}
{n} * {2} = {tab2}
{n} * {3} = {tab3}
{n} * {4} = {tab4}
{n} * {5} = {tab5}
{n} * {6} = {tab6}
{n} * {7} = {tab7}
{n} * {8} = {tab8}
{n} * {9} = {tab9}
{n} * {10} = {tab10}
'''))
