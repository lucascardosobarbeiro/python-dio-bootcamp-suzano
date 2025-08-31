nome = "Lucas"
idade = 19
profissao = "Estudante"
linguagem = "Python"

dados = {"nome": nome, "idade": idade,
         "profissao": profissao, "linguagem": linguagem}

# Old style formatting
print("Nome: %s Idade: %d Profissão: %s Linguagem: %s" %
      (nome, idade, profissao, linguagem))

# New style formatting
print("Nome: {0} Idade: {1} Profissão: {2} Linguagem: {3}".format(
    nome, idade, profissao, linguagem))

# f-strings (Python 3.6+)
print(
    f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}")

# Using dictionary with f-strings
print(f"Nome: {dados['nome']} Idade: {dados['idade']} Profissão: {dados['profissao']} Linguagem: {dados['linguagem']}")

# Multiline f-string
print(f"""  Nome: {nome}
Idade: {idade}  Profissão: {profissao} Linguagem: {linguagem}  """)

# Formatting numbers
num_1 = 100
num_2 = 3.151592653589793
print(f"{num_1:.2f}")  # Two decimal places
print(f"{num_2:.3f}")  # Three decimal places
