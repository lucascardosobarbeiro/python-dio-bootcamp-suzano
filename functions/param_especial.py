# Special parameters for models

# Positional-only parameters: must be passed by position
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# ---------  After the /, all parameters are keyword-only ---------


# Keyword-only parameters: must be passed by keyword
criar_carro("Corolla", 2020, "ABC-1234", marca="Toyota",
            motor=2.0, combustivel="Gasolina")

# All parameters can be passed only by keyword

# ---------  Before the * , all parameters are keyword-only ---------


def criar_moto(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# Example of creating a motorcycle in a database
criar_moto(modelo="Ninja", ano=2021, placa="XYZ-5678",
           marca="Kawasaki", motor=650, combustivel="Gasolina")

# Keyword and positional parameters HYBRID


def criar_caminhao(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# Example of creating a truck in a database
criar_caminhao("FH", 2019, "LMN-9101",
               marca="Volvo", motor=13, combustivel="Diesel")

# First class objects


def somar(a, b):
    return a + b

# Assigning the function to a variable


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado é: {resultado}")


#   Call the function by passing it as a parameter
exibir_resultado(10, 20, somar)

# local scope and global escope
