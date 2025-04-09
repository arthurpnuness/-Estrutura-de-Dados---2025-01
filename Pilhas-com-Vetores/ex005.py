def remover_item_meio(pilha, item):
    pilha_temp = Pilha(pilha.capacidade)
    encontrado = False
    
    # Procurando o item na pilha
    while not pilha.esta_vazia():
        elemento = pilha.desempilhar()
        if elemento == item and not encontrado:
            encontrado = True
            continue  # Não empilha na temp (remove)
        pilha_temp.empilhar(elemento)
    
    # Reempilhando os elementos
    while not pilha_temp.esta_vazia():
        pilha.empilhar(pilha_temp.desempilhar())
    
    return encontrado

# Testando a função
pilha = Pilha(10)
for i in [1, 2, 3, 4, 5]:
    pilha.empilhar(i)

print("Pilha original:")
while not pilha.esta_vazia():
    print(pilha.desempilhar())

# Reconstruindo a pilha
for i in [1, 2, 3, 4, 5]:
    pilha.empilhar(i)

# Removendo o número 3
removido = remover_item_meio(pilha, 3)
if removido:
    print("\nPilha após remover o 3:")
    while not pilha.esta_vazia():
        print(pilha.desempilhar())
else:
    print("Item não encontrado na pilha")