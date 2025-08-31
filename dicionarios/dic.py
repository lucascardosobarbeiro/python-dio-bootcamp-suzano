# Dictionaries

# dic nao ordenado chave valor { }

pessoa = {'nome': 'Lucas', 'idade': 28}
print(pessoa)

# Acessa valores do dic
pessoa['idade']
pessoa['nome']

# Altera valores dic
pessoa['nome'] = 'Maria'
print(pessoa)

# Outra forma de declarar
pessoa = dict(nome="lucas", idade=28)
print(pessoa)


# Dic Alinhados armzenam qualqer tipo de objeto em python desde que sejam imutáveis

contatos = {
    "lucas@barbeiro": {"nome": "lucas", "telefone": '111111-99999'},
    "lucas@cardoso": {"nome": "Gabriel", "telefone": '22221-99999'},
}


print(contatos['lucas@barbeiro']['telefone'])


# Iterar dicionarios - ele retorna valor da chave e nao o indice

# Não recomendados
for chave in contatos:
    print(chave, contatos[chave])

# Mais recomendado
for chave, valor in contatos.items():
    print(chave, valor)
