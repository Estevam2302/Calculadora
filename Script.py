print('Calculadora')
print('Tabela de operações')
print('Adição = a')
print('Subtração = s')
print('Divisão =  d')
print('Multiplicação = m')
print('Para sair insira "sair" na operação desejada')
while True:    
    operação = input('Escolha a operação desejada: ')
    if operação == ('sair'):
        print('Calculadora encerrada')    
        break
    n1 = int(input('Escolha o primeiro número: '))
    n2 = int(input('Escolha o segundo número: '))
    if operação == ('a'):
        print('%d + %d = '%(n1,n2),n1+n2)
    elif operação == ('s'):
        print('%d - %d = '%(n1,n2),n1-n2)
    elif operação == ('d'):
        print('%d / %d = '%(n1,n2),n1/n2)
    elif operação == ('m'):
        print('%d * %d = '%(n1,n2),n1*n2)
