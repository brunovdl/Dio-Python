menu = '''
BEM VINDO AO BANCO X

Escolha uma operação:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        print('=============== DEPÓSITO ===============')
        valor = float(input('Informe o valor do DEPÓSITO => R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'DEPÓSITO => R$ {valor:.2f}\n'
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Falha na operação! Valor informado é inválido.')

    elif opcao == '2':
        print('=============== SAQUE ===============')
        valor = float(input('Informe o valor do SAQUE => R$ '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f'Falha na operação! Seu saldo é de R${saldo:.2f} Saldo insuficiente.')
        elif excedeu_limite:
            print('Falha na operação! Valor excede o limite.')
        elif excedeu_saques:
            print('Falha na operação! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'SAQUE => R$ {valor:.2f}\n'
            numero_saques += 1
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Falha na operação! Valor informado é inválido.')

    elif opcao == '3':
        print('=============== EXTRATO ===============')
        print('Não foram registradas movimentações.' if not extrato else extrato)
        print(f'\nSALDO => R$ {saldo:.2f}')
        print('=======================================')

    elif opcao == '0':
        break

    else:
        print('OPERAÇÃO INVÁLIDA, RETORNANDO AO MENU INICIAL.')
