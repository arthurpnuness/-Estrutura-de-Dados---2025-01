class NoCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplaCircular:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        novo = NoCircular(valor)
        if not self.inicio:
            novo.proximo = novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior
            novo.proximo = self.inicio
            novo.anterior = ultimo
            ultimo.proximo = self.inicio.anterior = novo
            self.inicio = novo

    def imprimir(self):
        if not self.inicio:
            return
        atual = self.inicio
        while True:
            print(atual.dado, end=" ")
            atual = atual.proximo
            if atual == self.inicio:
                break
        print()

    def buscar(self, valor):
        if not self.inicio:
            return None
        atual = self.inicio
        while True:
            if atual.dado == valor:
                return atual
            atual = atual.proximo
            if atual == self.inicio:
                break
        return None

    def remover(self, valor):
        no = self.buscar(valor)
        if not no:
            return False
        if no.proximo == no:  # único elemento
            self.inicio = None
        else:
            no.anterior.proximo = no.proximo
            no.proximo.anterior = no.anterior
            if no == self.inicio:
                self.inicio = no.proximo
        return True

    def inserir_fim(self, valor):
        if not self.inicio:
            self.inserir_inicio(valor)
        else:
            novo = NoCircular(valor)
            ultimo = self.inicio.anterior
            novo.proximo = self.inicio
            novo.anterior = ultimo
            ultimo.proximo = self.inicio.anterior = novo

    def inserir_ordenado(self, valor):
        if not self.inicio or self.inicio.dado >= valor:
            self.inserir_inicio(valor)
            return
        atual = self.inicio
        while atual.proximo != self.inicio and atual.proximo.dado < valor:
            atual = atual.proximo
        novo = NoCircular(valor)
        novo.proximo = atual.proximo
        novo.anterior = atual
        atual.proximo.anterior = novo
        atual.proximo = novo

    def imprimir_inverso(self):
        if not self.inicio:
            return
        atual = self.inicio.anterior
        while True:
            print(atual.dado, end=" ")
            atual = atual.anterior
            if atual == self.inicio.anterior:
                break
        print()
