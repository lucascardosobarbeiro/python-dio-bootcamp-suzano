# --- MÓDULOS E BIBLIOTECAS ---
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# --- CLASSES DO MODELO DE DADOS (A LÓGICA DO NEGÓCIO) ---


class Cliente:
    """
    Classe base para representar um cliente do banco.
    Armazena informações básicas e a lista de contas associadas.
    """

    def __init__(self, endereco: str):
        self.endereco: str = endereco
        self.contas: List[Conta] = []

    def realizar_transacao(self, conta: 'Conta', transacao: 'Transacao'):
        """Delega a responsabilidade de registrar a transação para o objeto 'transacao'."""
        transacao.registrar(conta)

    def adicionar_conta(self, conta: 'Conta'):
        """Associa uma nova conta a este cliente."""
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Especialização da classe Cliente para representar uma Pessoa Física.
    Herda de Cliente e adiciona atributos específicos.
    """

    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        super().__init__(endereco)  # Chama o construtor da classe pai
        self.nome: str = nome
        self.data_nascimento: str = data_nascimento
        self.cpf: str = cpf


class Conta:
    """
    Classe que representa a conta bancária de um cliente.
    Contém a lógica para operações de saque e depósito e gerencia o saldo e o histórico.
    """

    def __init__(self, numero: int, cliente: Cliente):
        self._saldo: float = 0.0
        self._numero: int = numero
        self._agencia: str = "0001"
        self._cliente: Cliente = cliente
        self._historico: Historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> 'Conta':
        """Método de fábrica para criar instâncias da classe de forma flexível."""
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        """Permite o acesso ao saldo, mas não a sua modificação direta (encapsulamento)."""
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> 'Historico':
        return self._historico

    def sacar(self, valor: float) -> bool:
        """Implementa a lógica de saque com validações básicas."""
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor: float) -> bool:
        """Implementa a lógica de depósito."""
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True

        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False


class ContaCorrente(Conta):
    """
    Especialização da classe Conta.
    Adiciona regras de negócio específicas para contas correntes.
    """

    def __init__(self, numero: int, cliente: Cliente, limite: float = 500.0, limite_saques: int = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        """
        Sobrescreve o método 'sacar' (Polimorfismo).
        Aplica regras da ContaCorrente antes de chamar a lógica da classe pai.
        """
        saques_realizados_hoje = len(
            [t for t in self.historico.transacoes if t["tipo"] ==
                Saque.__name__ and t["data"].date() == datetime.now().date()]
        )

        if valor > self._limite:
            print(
                f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {self._limite:.2f}. @@@")
            return False

        if saques_realizados_hoje >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
            return False

        # Se passou nas validações, chama o método 'sacar' da classe pai (Conta).
        return super().sacar(valor)

    def __str__(self) -> str:
        """Define uma representação em string legível para o objeto."""
        return f"Agência: {self.agencia}\nC/C:     {self.numero}\nTitular: {self.cliente.nome}"


class Historico:
    """Gerencia o histórico de transações de uma conta."""

    def __init__(self):
        self._transacoes: List[dict] = []

    @property
    def transacoes(self) -> List[dict]:
        return self._transacoes

    def adicionar_transacao(self, transacao: 'Transacao'):
        """Adiciona uma nova transação à lista."""
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(),
            }
        )


class Transacao(ABC):
    """
    Classe Abstrata Base (ABC) para Transação.
    Define um "contrato" que todas as classes de transação devem seguir.
    """
    @property
    @abstractmethod
    def valor(self) -> float:
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass


class Saque(Transacao):
    """Classe que representa a transação de saque."""

    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        """Tenta realizar o saque e, se bem-sucedido, registra no histórico."""
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """Classe que representa a transação de depósito."""

    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta: Conta):
        """Tenta realizar o depósito e, se bem-sucedido, registra no histórico."""
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# --- FUNÇÕES DE INTERAÇÃO COM O USUÁRIO (CONTROLADOR / VISÃO) ---

def menu():
    """Exibe o menu principal e retorna a opção do usuário."""
    menu_texto = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    ======================================
    => """
    return input(menu_texto)


def buscar_cliente(cpf: str, clientes: List[PessoaFisica]):
    """Busca um cliente na lista a partir do CPF."""
    clientes_filtrados = [c for c in clientes if c.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def operacao_transacao(clientes: List[PessoaFisica], tipo_transacao):
    """Função genérica para gerenciar depósitos e saques."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    if not cliente.contas:
        print("\n@@@ Este cliente não possui uma conta cadastrada. @@@")
        return

    # Lógica para escolher a conta (simplificado para pegar a primeira)
    conta_cliente = cliente.contas[0]

    try:
        valor = float(input("Informe o valor: "))
        # Cria um objeto Saque() ou Deposito()
        transacao = tipo_transacao(valor)
        cliente.realizar_transacao(conta_cliente, transacao)
    except ValueError:
        print("\n@@@ Valor inválido. A operação foi cancelada. @@@")


def exibir_extrato(clientes: List[PessoaFisica]):
    """Exibe o extrato da conta de um cliente."""
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    if not cliente.contas:
        print("\n@@@ Este cliente não possui uma conta cadastrada. @@@")
        return

    conta_cliente = cliente.contas[0]

    print("\n================ EXTRATO ================")
    print(f"Titular: {cliente.nome}")
    print(f"Agência: {conta_cliente.agencia} | Conta: {conta_cliente.numero}")
    print("------------------------------------------")

    transacoes = conta_cliente.historico.transacoes
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for t in transacoes:
            tipo_transacao = t['tipo']
            valor_transacao = t['valor']
            data_transacao = t['data'].strftime("%d-%m-%Y %H:%M:%S")
            print(
                f"{data_transacao} - {tipo_transacao:<10s} - R$ {valor_transacao:10.2f}")

    print("------------------------------------------")
    print(f"Saldo Final: R$ {conta_cliente.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes: List[PessoaFisica]):
    """Cria e adiciona um novo cliente à lista."""
    cpf = input("Informe o CPF (somente números): ")
    if buscar_cliente(cpf, clientes):
        print("\n@@@ Já existe um cliente com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(novo_cliente)
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(contas: List[Conta], clientes: List[PessoaFisica]):
    """Cria uma nova conta corrente e a vincula a um cliente."""
    cpf = input("Informe o CPF do cliente para vincular a conta: ")
    cliente = buscar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! Não é possível criar a conta. @@@")
        return

    numero_conta = len(contas) + 1
    nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(nova_conta)
    cliente.adicionar_conta(nova_conta)

    print("\n=== Conta criada com sucesso! ===")
    print("--- Dados da Nova Conta ---")
    print(str(nova_conta))
    print("---------------------------")


def listar_contas(contas: List[Conta]):
    """Lista todas as contas cadastradas."""
    if not contas:
        print("\n@@@ Nenhuma conta foi cadastrada ainda. @@@")
        return

    print("\n--- Lista de Contas Cadastradas ---")
    for conta in contas:
        print(str(conta))
        print("-----------------------------------")


def main():
    """Função principal que executa o loop do sistema bancário."""
    clientes: List[PessoaFisica] = []
    contas: List[Conta] = []

    while True:
        opcao = menu()

        if opcao == "d":
            operacao_transacao(clientes, Deposito)
        elif opcao == "s":
            operacao_transacao(clientes, Saque)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            criar_conta(contas, clientes)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break
        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
