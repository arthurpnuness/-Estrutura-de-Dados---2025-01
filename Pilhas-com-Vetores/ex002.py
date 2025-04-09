def esvaziar_pilha(pilha):
    while not pilha.esta_vazia():
        pilha.desempilhar()
    print("Pilha esvaziada")

# Testando a função
pilha = Pilha(5)
for i in range(1, 4):
    pilha.empilhar(i)

esvaziar_pilha(pilha)