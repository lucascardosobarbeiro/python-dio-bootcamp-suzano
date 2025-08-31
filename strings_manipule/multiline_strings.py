# Triple strings can span multiple lines
mensagem = """Olá, tudo bem?
Eu estou aprendendo Python.             
Estou gostando muito!"""

print(f"mensagem completa: {mensagem}")  # Full message
print(f"Tamanho da mensagem: {len(mensagem)}")  # Length of the string
print(f"Conta os O´S: {mensagem.count("o")}")  # Count occurrences of 'o'
# Split the string into words
print(f"Divide a string em palavras {mensagem.split()}")
print(mensagem.splitlines())  # Split the string into lines
