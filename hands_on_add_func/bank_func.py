# Importa a biblioteca datetime para trabalhar com datas e horas
from datetime import datetime

# --- FUNÇÕES DE CADASTRO (NOVAS) ---


def cadastrar_cliente(clientes):
    """
    Cadastra um novo cliente (usuário) no sistema.
    Não permite CPFs duplicados.
    """
    cpf = input("Informe o CPF (somente números): ")

    # Procura se o cliente já existe na lista
    cliente_encontrado = buscar_cliente_por_cpf(cpf, clientes)
    if cliente_encontrado:
        print("\n@@@ Já existe um cliente com este CPF! @@@")
        return  # Encerra a função

    # Pede o restante dos dados se o CPF for único
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Cria um dicionário para o novo cliente
    novo_cliente = {"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco}

    # Adiciona o novo cliente à lista de clientes
    clientes.append(novo_cliente)

    print("\n=== Cliente cadastrado com sucesso! ===")


def cadastrar_conta(contas, clientes):
    """
    Cria uma nova conta bancária vinculada a um cliente existente.
    """
    cpf = input("Informe o CPF do cliente para vincular a conta: ")

    cliente_encontrado = buscar_cliente_por_cpf(cpf, clientes)

    if not cliente_encontrado:
        print("\n@@@ Cliente não encontrado! Não é possível criar a conta. @@@")
        return  # Encerra a função se o cliente não existir

    # Cria os dados da nova conta
    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "cpf_cliente": cpf,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0,
        "numero_transacoes_hoje": 0,
        "data_atual": datetime.now().date()
    }

    # Adiciona a nova conta à lista de contas
    contas.append(nova_conta)

    print("\n=== Conta criada com sucesso! ===")
    print(
        f"Agência: {nova_conta['agencia']}, Conta: {nova_conta['numero_conta']}")


def buscar_cliente_por_cpf(cpf, clientes):
    """
    Função auxiliar para encontrar um cliente na lista a partir do CPF.
    Retorna o dicionário do cliente se encontrar, ou None se não encontrar.
    """
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


# --- FUNÇÕES DE OPERAÇÃO (ATUALIZADAS) ---

def menu():
    """
    Exibe o menu de opções para o usuário (com novas opções).
    """
    menu_texto = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(menu_texto)


def depositar(conta, valor):
    """
    Realiza a operação de depósito na conta informada.
    Recebe um dicionário 'conta' para modificar.
    """
    if valor > 0:
        conta["saldo"] += valor
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        conta["extrato"] += f"{timestamp} - Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return conta


def sacar(conta, valor, limite_saque, limite_saques_diarios):
    """
    Realiza a operação de saque da conta informada.
    Recebe um dicionário 'conta' para modificar.
    """
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite_saque
    excedeu_saques = conta["numero_saques"] >= limite_saques_diarios

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print(
            f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite_saque:.2f}. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
    elif valor > 0:
        conta["saldo"] -= valor
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        conta["extrato"] += f"{timestamp} - Saque:\t\tR$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return conta


def exibir_extrato(conta):
    """
    Exibe o extrato da conta informada.
    """
    print("\n================ EXTRATO ================")
    print(f"Conta: {conta['numero_conta']} | Agência: {conta['agencia']}")
    print("------------------------------------------")
    print(
        "Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo:\t\tR$ {conta['saldo']:.2f}")
    print("==========================================")


# --- FUNÇÃO PRINCIPAL (ATUALIZADA) ---

def main():
    """
    Função principal que executa o sistema bancário.
    """
    # Constantes do sistema
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500
    LIMITE_TRANSACOES = 10

    # Estruturas de dados para armazenar clientes e contas
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            cadastrar_cliente(clientes)

        elif opcao == "nc":
            cadastrar_conta(contas, clientes)

        elif opcao in ("d", "s", "e"):
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente_por_cpf(cpf, clientes)

            if not cliente:
                print("\n@@@ Cliente não encontrado! @@@")
                continue

            # Acha a primeira conta associada ao CPF (pode ser melhorado para clientes com múltiplas contas)
            conta_cliente = None
            for conta in contas:
                if conta["cpf_cliente"] == cpf:
                    conta_cliente = conta
                    break

            if not conta_cliente:
                print("\n@@@ Nenhuma conta bancária encontrada para este cliente! @@@")
                continue

            # Verifica e reseta os limites diários se o dia mudou
            if datetime.now().date() != conta_cliente["data_atual"]:
                conta_cliente["data_atual"] = datetime.now().date()
                conta_cliente["numero_saques"] = 0
                conta_cliente["numero_transacoes_hoje"] = 0
                print(
                    "\n=== Um novo dia começou! Seus limites diários foram resetados. ===")

            # Roteamento das operações
            if opcao == "d":
                if conta_cliente["numero_transacoes_hoje"] >= LIMITE_TRANSACOES:
                    print("\n@@@ Você atingiu o limite de 10 transações diárias! @@@")
                    continue

                try:
                    valor = float(input("Informe o valor do depósito: "))
                    valor_antes = conta_cliente["saldo"]
                    conta_cliente = depositar(conta_cliente, valor)
                    if conta_cliente["saldo"] > valor_antes:
                        conta_cliente["numero_transacoes_hoje"] += 1
                except ValueError:
                    print("\n@@@ Entrada inválida. Por favor, digite um número. @@@")

            elif opcao == "s":
                if conta_cliente["numero_transacoes_hoje"] >= LIMITE_TRANSACOES:
                    print("\n@@@ Você atingiu o limite de 10 transações diárias! @@@")
                    continue

                try:
                    valor = float(input("Informe o valor do saque: "))
                    saques_antes = conta_cliente["numero_saques"]
                    conta_cliente = sacar(
                        conta_cliente, valor, LIMITE_POR_SAQUE, LIMITE_SAQUES)
                    if conta_cliente["numero_saques"] > saques_antes:
                        conta_cliente["numero_transacoes_hoje"] += 1
                except ValueError:
                    print("\n@@@ Entrada inválida. Por favor, digite um número. @@@")

            elif opcao == "e":
                exibir_extrato(conta_cliente)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
