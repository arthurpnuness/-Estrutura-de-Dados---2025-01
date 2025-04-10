import random

class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None

class RoletaRussaCircular:
    def __init__(self):
        self.inicio = None

    def adicionar_guerreiro(self, nome):
        novo = Guerreiro(nome)
        if not self.inicio:
            novo.proximo = novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior
            novo.proximo = self.inicio
            novo.anterior = ultimo
            ultimo.proximo = self.inicio.anterior = novo

    def remover(self, guerreiro):
        if guerreiro.proximo == guerreiro:
            self.inicio = None
        else:
            guerreiro.anterior.proximo = guerreiro.proximo
            guerreiro.proximo.anterior = guerreiro.anterior
            if guerreiro == self.inicio:
                self.inicio = guerreiro.proximo

    def contar(self):
        if not self.inicio:
            return 0
        contador = 1
        atual = self.inicio.proximo
        while atual != self.inicio:
            contador += 1
            atual = atual.proximo
        return contador

    def rodar_jogo(self):
        while self.contar() > 1:
            total = self.contar()
            passos = random.randint(1, total)
            atual = self.inicio
            for _ in range(passos - 1):
                atual = atual.proximo
            print(f"💀 Guerreiro eliminado: {atual.nome}")
            self.remover(atual)
        print(f"🏆 Sobrevivente: {self.inicio.nome}")
