eextract = 0
withdraw_limit = 3
withdraw_register = []
deposit_register = []

print("\033[34m Bem vindo ao DIO Bank!\033[m")

while True:
    print('''\033[35m=======================================
|               Menu:                 |
=======================================\033[m
\033[34m
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair\033[m\n''')

    option = (input('Digite a opção desejada: '))

    if option == '1':
        deposit = float(input('Digite o valor do depósito: ').replace(',', '.'))
        if deposit > 0:
            extract += deposit
            print(f'Depósito de R${deposit:.2f} realizado com sucesso.')
            deposit_register.append(f'Depósito de R${deposit:.2f} realizado.')
        else:
            print('\033[31mValor inválido. O depósito deve ser maior que zero.\033[m')
        while True:
            finish = input('Deseja realizar mais alguma operação? (S/N): ').strip().upper()
            if finish not in ['S', 'N']:
                print('\033[31mOpção inválida, por favor digite S para sim ou N para não.\033[m')
            else:
                break
        if finish == 'N':
            break

    elif option == '2':
        withdraw = float(input('Digite o valor do saque: ').replace(',', '.'))
        if withdraw_limit > 0:
            if withdraw > extract:
                print('\033[31mSaldo insuficiente para saque.\033[m')
            elif withdraw > 500:
                print('\033[31mValor do saque excede o limite de R$500,00 por saque.\033[m')
            else:
                print(f'Saque de R${withdraw:.2f} realizado com sucesso.')
                extract -= withdraw
                withdraw_limit -= 1
                withdraw_register.append(f'Saque de R${withdraw:.2f} realizado.')
                print(f'Você ainda pode realizar {withdraw_limit} saques hoje.')
        else:
            print('\033[31mLimite de saques diários atingido. Tente novamente amanhã.\033[m')

        while True:
            finish = input('Deseja realizar mais alguma operação? (S/N): ').strip().upper()
            if finish not in ['S', 'N']:
                print('\033[31mOpção inválida, por favor digite S para sim ou N para não.\033[m')
            else:
                break
        if finish == 'N':
            break

    elif  option == '3':
        if deposit_register:
            print('\033[32mExtrato de Depósitos:\033[m')
            for record in deposit_register:
                print(record)
        else:
            print('Nenhum depósito realizado hoje.')
        print('================================')
        if withdraw_register:
            print('\033[32mExtrato de Saques:\033[m')
            for record in withdraw_register:
                print(record)
        else:
            print('Nenhum saque realizado hoje.')
        print('================================')
        print(f'Seu saldo atual é de R${extract:.2f}')

        while True:
            finish = input('Deseja realizar mais alguma operação? (S/N): ').strip().upper()
            if finish not in ['S', 'N']:
                print('\033[31mOpção inválida, por favor digite S para sim ou N para não.\033[m')
            else:
                break
        if finish == 'N':
            break

    elif option == '4':
        break

    else:
        print('\033[31mOpção inválida, por favor escolha entre 1 e 4.\033[m')

print('\033[35m Obrigado por usar o DIO Bank!\033[m')
