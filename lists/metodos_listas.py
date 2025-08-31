# --------------- LIST CLASS METHODS --------------
# APPEND - ADICIONA UM ITEM AO FINAL DA LISTA
# CLEAR - REMOVE TODOS OS ITENS DA LISTA
# COPY - RETORNA UMA CÓPIA RASA DA LISTA
# COUNT - RETORNA O NÚMERO DE VEZES QUE UM ITEM AP
# EXTEND - ADICIONA TODOS OS ITENS DE UMA LISTA (OU OUTRO ITERÁVEL) AO FINAL DA LISTA ATUAL

# Append - Adiciona um item ao final da lista
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

# Copy - Cópia rasa (shallow copy)
lista_copiada = lista.copy()
print(lista_copiada)
print(lista is lista_copiada)  # False, são objetos diferentes

# Count - Conta quantas vezes um elemento aparece na lista
print(lista.count(1))  # 1
print(lista.count("Python"))  # 1
print(lista.count("Java"))  # 0

# Extend - Adiciona os elementos de uma lista (ou outro iterável) ao final da lista atual
lista.extend([2, 3, 4])  # Adiciona múltiplos elementos  de uma vez
print(lista)

# Clear - Remove todos os itens da lista
lista.clear()
print(lista)  # Lista vazia

# OBS: OUTROS MÉTODOS DE LISTA
# index - Retorna o índice do primeiro elemento com o valor especificado
# insert - Adiciona um elemento em uma posição específica
# pop - Remove o elemento na posição especificada (ou o último elemento, se nenhum índice
# remove - Remove o primeiro item com o valor especificado
# reverse - Inverte a ordem dos elementos na lista
# sort - Ordena os elementos da lista (opcionalmente, pode receber uma função de chave)
# len - Retorna o número de itens na lista
# sum - Retorna a soma dos elementos da lista (se forem numéricos)
# min - Retorna o menor valor na lista (se forem numéricos)
# max - Retorna o maior valor na lista (se forem numéricos)
# sorted - Retorna uma nova lista ordenada a partir dos elementos da lista original
# list - Converte um iterável (como uma string ou tupla) em uma lista
