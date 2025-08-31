# --------------- Tuplas --------------- #
# Tuplas são usadas para armazenar múltiplos itens em uma única variável.
# Tuplas são imutáveis, ou seja, não podem ser alteradas após a criação
# Tuplas são definidas usando parênteses ()
# Tuplas podem conter diferentes tipos de dados

#  Declaração de valores
frutas = ('maçã', 'banana', 'laranja', 'uva')

# Apresentnado no console
print(frutas[0])
print(frutas[2])

letras = tuple('python')

numeros = tuple(range(10))

paises = ('Brasil', 'Argentina', 44, 55, True)
print(isinstance(paises, tuple))

# Tuplas aninhadas armazenam outras tuplas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0]  # (1, "a", 2)
matriz[0][0]  # 1
matriz[0][-1]  # 2
matriz[-1][-1]  # "c"


carros = ("gol")
print(isinstance(carros, tuple))
