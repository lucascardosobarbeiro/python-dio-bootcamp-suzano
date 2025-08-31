# Conjuntos
# --------- SETS -------- NÃO POSUI OBJETOS REPETIDOS, eliminar obj repetidos

numeros = set([1, 2, 3, 4, 4, 3])  # {1,2,3,4}
print(numeros)

frutas = set("Abacaxi")  # { "b", "a" ...} remove os a
print(frutas)

carros = set(("Palio", "Gol", "Palio"))
print(carros)

# Com listas é possível também
linguagens = {"python", "java", "python"}
print(linguagens)


# ------------ ACESSANDO DADOS NO SET -----------
# Não é possível acessar via indice os valores, para isso precisamos converter o set para uma list
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])

# --------- Percorrer set (interar) ------------
carros = {"Gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# METODOS DE CLASSE
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))
