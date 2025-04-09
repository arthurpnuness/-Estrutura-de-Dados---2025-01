class EditorTexto:
    def __init__(self):
        self.pilha = Pilha(1000)  # Capacidade grande para texto

    def digitar(self):
        print("Digite seu texto (use # para undo, @ para sair):")
        while True:
            caractere = input("Digite um caractere: ")[0]
            if caractere == '@':
                break
            elif caractere == '#':
                if not self.pilha.esta_vazia():
                    self.pilha.desempilhar()
                    print("Último caractere removido")
            else:
                self.pilha.empilhar(caractere)
            self.mostrar_texto()

    def mostrar_texto(self):
        print("Texto atual:", self.obter_texto())

    def obter_texto(self):
        texto = []
        temp_pilha = Pilha(self.pilha.capacidade)
        
        # Desempilha para uma pilha temporária
        while not self.pilha.esta_vazia():
            caractere = self.pilha.desempilhar()
            temp_pilha.empilhar(caractere)
        
        # Reempilha e constrói o texto
        texto_str = ""
        while not temp_pilha.esta_vazia():
            caractere = temp_pilha.desempilhar()
            self.pilha.empilhar(caractere)
            texto_str += caractere
        
        return texto_str

# Usando o editor
editor = EditorTexto()
editor.digitar()