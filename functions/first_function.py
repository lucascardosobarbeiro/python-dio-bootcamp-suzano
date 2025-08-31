# learning Functions in Python
def show_message():
    print("Hello from the first function!")


def show_message_2(name):
    print(f"Hello, {name}!")


def show_message_3(name="Guest"):
    print(f"Hello, {name}!")


show_message()
show_message_2("Lucas")
show_message_3()
show_message_3("Alice")


def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


print(calcular_total([10, 20, 30, 40, 50]))
print(retorna_antecessor_sucessor(10))

# Example of a function that simulates saving a car to a database


def save_car(marca, modelo, ano, placa):

    # Simulating saving a car to a database
    print(f" Car saved: {marca} {modelo} {ano} {placa}")


# This way is not recommended for production code, but it is useful for learning
save_car("Toyota", "Corolla", 2020, "ABC-1234")

# Using keyword arguments
save_car(marca="Honda", modelo="Civic", ano=2019, placa="XYZ-5678")

# Using a dictionary and unpacking it with **
save_car(**{"marca": "Ford", "modelo": "Focus",
         "ano": 2018, "placa": "LMN-9101"})

# Using args and kwargs

# Example of a function that prints a poem with metadata


def show_poema(date_extense, *args, **kwargs):
    # Join all positional arguments into a single text block
    text = "\n".join(args)
    # Create metadata from keyword arguments
    meta_dados = "\n".join(
        # List comprehension
        [f"{chave}: {valor}" for chave, valor in kwargs.items()])
    message = (f"{date_extense}\n\n{text}\n\n{meta_dados}")  # f-string
    print(message)


# Calling the function with a poem and metadata
show_poema(
    "October 5, 2023",
    "Roses are red,",
    "Violets are blue,",
    "Sugar is sweet,",
    "And so are you.",
    author="John Doe",
    length="4 lines"
)
