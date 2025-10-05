# Sistema bancário com funcionalidades de depósito, saque e extrato.

MENU = """
\n=========== MENU ===========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=============================
=> """

LIMITE_SAQUE = 500
MAX_SAQUES_DIARIOS = 3

def exibir_extrato(saldo, extrato):
    print("\n=========== EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("================================")

def realizar_deposito(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
    return saldo, extrato

def realizar_saque(saldo, extrato, numero_saques):
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > LIMITE_SAQUE:
            print("Operação falhou! Valor excede o limite por saque.")
        elif numero_saques >= MAX_SAQUES_DIARIOS:
            print("Operação falhou! Número máximo de saques diários atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
    return saldo, extrato, numero_saques

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = input(MENU).strip().lower()

        if opcao == "d":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()