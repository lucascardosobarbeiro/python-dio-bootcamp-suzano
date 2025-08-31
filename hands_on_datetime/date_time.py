# Importa a biblioteca datetime para trabalhar com datas e horas
from datetime import datetime


def menu():
    """
    Exibe o menu de opções para o usuário.
    """
    menu_texto = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(menu_texto)


def depositar(saldo, valor, extrato):
    """
    Realiza a operação de depósito na conta.
    Agora, adiciona a data e hora da transação ao extrato.
    """
    if valor > 0:
        saldo += valor
        # Adiciona a data e hora formatadas ao registro do extrato
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        extrato += f"{timestamp} - Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque da conta, com validações.
    Agora, adiciona a data e hora da transação ao extrato.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        # Adiciona a data e hora formatadas ao registro do extrato
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        extrato += f"{timestamp} - Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    """
    Exibe o extrato da conta com as transações e o saldo.
    O extrato agora contém data e hora.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def main():
    """
    Função principal que executa o sistema bancário.
    """
    # Constantes do sistema
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500
    LIMITE_TRANSACOES = 10  # Novo limite de 10 transações diárias

    # Variáveis de estado da conta
    saldo = 0
    extrato = ""

    # Variáveis de controle diário
    numero_saques = 0
    numero_transacoes_hoje = 0
    data_atual = datetime.now().date()  # Armazena a data atual

    while True:
        # Verifica se o dia mudou para resetar os limites diários
        if datetime.now().date() != data_atual:
            data_atual = datetime.now().date()  # Atualiza para o novo dia
            numero_saques = 0                 # Zera o contador de saques do dia
            numero_transacoes_hoje = 0        # Zera o contador de transações do dia
            print("\n=== Um novo dia começou! Seus limites diários foram resetados. ===")

        opcao = menu()

        if opcao == "d":
            # Verifica se o limite de transações diárias foi atingido
            if numero_transacoes_hoje >= LIMITE_TRANSACOES:
                print("\n@@@ Você atingiu o limite de 10 transações diárias! @@@")
                continue  # Volta para o menu

            try:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

                # Se o depósito foi válido, incrementa o contador de transações
                if valor > 0:
                    numero_transacoes_hoje += 1
            except ValueError:
                print("\n@@@ Entrada inválida. Por favor, digite um número. @@@")

        elif opcao == "s":
            # Verifica se o limite de transações diárias foi atingido
            if numero_transacoes_hoje >= LIMITE_TRANSACOES:
                print("\n@@@ Você atingiu o limite de 10 transações diárias! @@@")
                continue  # Volta para o menu

            try:
                valor = float(input("Informe o valor do saque: "))

                saques_antes = numero_saques
                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=LIMITE_POR_SAQUE,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                )

                # Se um saque foi efetuado com sucesso, incrementa o contador de transações
                if numero_saques > saques_antes:
                    numero_transacoes_hoje += 1
            except ValueError:
                print("\n@@@ Entrada inválida. Por favor, digite um número. @@@")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
