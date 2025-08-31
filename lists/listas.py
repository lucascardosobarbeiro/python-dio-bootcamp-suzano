# Lists
# ----------- How to Create a list value -----------
# Lists are used to store multiple items in a single variable.
frutas = ['maçã', 'banana', 'laranja', 'uva']
print(frutas)

# An empty list
frutas = []
print(frutas)

# Lists can contain different data types
letras = list('python')
print(letras)

# A list of numbers from 0 to 9
numeros = list(range(10))
print(numeros)

# A list with mixed data types
carro = ['Ford', 'F8', 50, 2020, 'preto', 4, True]
print(carro)

# ----------- Accessing List Elements -----------
# Lists are ordered, changeable, and allow duplicate values.
# You can access list items by referring to their index number, starting at index 0.

frutas = ['maçã', 'banana', 'laranja', 'uva']
print(frutas[0])  # First item
print(frutas[1])  # Second item

# Matrizs (2D Lists) We use two sets of brackets, usually called a list of lists.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0][0])  # First row, first column
print(matriz[1][2])  # Second row, third column
print(matriz[2][1])  # Third row, second column
print(matriz[2])     # Third row

# ----------Slicing lists ----------
# You can return a range of list items by specifying where to start and end the range.
frutas = ['maçã', 'banana', 'laranja', 'uva', 'pera', 'kiwi']
print(frutas[1:4])  # From index 1 to 3 (not including index 4)
print(frutas[:3])   # From the beginning to index 2
print(frutas[2:])   # From index 2 to the end
print(frutas[-1])   # Last item

# Interation lists
for fruta in frutas:
    print(fruta)  # Looping through the list
for index, fruta in enumerate(frutas):  # Looping with index
    print(index, fruta)  # Looping with index
for index in range(len(frutas)):  # Looping with index using range
    print(index, frutas[index])

# ----------- Compreension lists ------------
# A list comprehension is a shorter syntax to create a new list based on the values of an existing list.
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]  # Create a list of squares
print(quadrados)
pares = [x for x in numeros if x % 2 == 0]  # Create a list of even numbers
print(pares)
# Create a list of uppercase fruits
maiusculas = [fruta.upper() for fruta in frutas]
print(maiusculas)
print([x*2 for x in range(10)])  # Create a list of numbers multiplied by 2
# Create a list of squares of even numbers
print([x**2 for x in range(10) if x % 2 == 0])
print([letra for letra in 'python'])  # Create a list of letters in a string
