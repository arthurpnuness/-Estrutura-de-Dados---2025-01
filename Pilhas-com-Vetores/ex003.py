pilha_numeros = Pilha(5)

# Solicitando 5 números ao usuário
print("Digite 5 números:")
for _ in range(5):
    numero = int(input())
    pilha_numeros.empilhar(numero)

# Mostrando na ordem inversa
print("Números na ordem inversa:")
while not pilha_numeros.esta_vazia():
    print(pilha_numeros.desempilhar())