menu = """
[1] Depositar / [2] Sacar / [3] Extrato / [4] Sair
"""

saldo = 0
deposito = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    selecione = input(menu)

    if selecione == '1':
        deposito = float(input('Quanto você quer depositar? R$'))

        if deposito > 0:
            saldo = saldo + deposito
            print(f'Saldo: R${saldo}')
            extrato += (f'\nDepósito: R$ {deposito:.2f}')
        else:
            print('Digite um valor válido')

    elif selecione == '2':

        while True:
            if numero_saques >= LIMITE_SAQUES:
                print('Limite máximo de saques')
                break

            saque = float(input('Qual valor deseja sacar? R$'))

            if saque > saldo:
                print('Não foi possível realizar essa transação, saldo indisponível')
                break

            if saque >= 500:
                print('Máximo R$500,00 reais por saque')
                break

            if saque > 0:
                if saque > 0 and deposito == 0:
                    break
                else:
                    saldo = saldo - saque
                    extrato += (f'\nSaque: R$ -{saque}')
                    print(f'Saldo: R${saldo}')
                    numero_saques += 1
                    break
            else:
                print('Valor informado inválido!')
    elif selecione == '3':
        print('==============EXTRATO')
        print('Não foram realizados movimentações em sua conta.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=========================================')

    elif selecione == '4':
        print('Aguarde...')
        break
    else:
        print('Operação inválida')