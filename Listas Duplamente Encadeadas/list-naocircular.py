class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDupla:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        if self.inicio:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
        self.inicio = novo

    def imprimir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()

    def buscar(self, valor):
        atual = self.inicio
        while atual:
            if atual.dado == valor:
                return atual
            atual = atual.proximo
        return None

    def remover(self, valor):
        atual = self.buscar(valor)
        if not atual:
            return False
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.inicio = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        return True

    def inserir_fim(self, valor):
        novo = No(valor)
        if not self.inicio:
            self.inicio = novo
            return
        atual = self.inicio
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo
        novo.anterior = atual

    def inserir_ordenado(self, valor):
        novo = No(valor)
        if not self.inicio or self.inicio.dado >= valor:
            self.inserir_inicio(valor)
            return
        atual = self.inicio
        while atual.proximo and atual.proximo.dado < valor:
            atual = atual.proximo
        novo.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = novo
        novo.anterior = atual
        atual.proximo = novo
