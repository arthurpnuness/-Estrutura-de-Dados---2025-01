class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = [None] * capacidade

    def empilhar(self, valor):
        if self.topo == self.capacidade - 1:
            print("Pilha cheia!")
            return False
        self.topo += 1
        self.valores[self.topo] = valor
        return True

    def desempilhar(self):
        if self.topo == -1:
            print("Pilha vazia!")
            return None
        valor = self.valores[self.topo]
        self.topo -= 1
        return valor

    def esta_vazia(self):
        return self.topo == -1

# Criando pilha e empilhando números de 1 a 5
pilha = Pilha(10)
for i in range(1, 6):
    pilha.empilhar(i)

# Desempilhando e mostrando os elementos
while not pilha.esta_vazia():
    print(pilha.desempilhar())