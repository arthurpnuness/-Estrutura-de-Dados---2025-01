class Node:
    def __init__(self, value):  # __init__ cria um novo nó
        self.value = value  # Armazena o valor do nó
        self.next = None  # Ponteiro inicialmente não aponta para nada (None), porque ainda não sabemos o próximo

class Linked_list:
    def __init__(self):
        self.head = None  # Aqui guardamos a referência do primeiro nó da lista

    def insert(self, value):
        # Insere um novo nó no início da lista.
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node  # Novo nó se torna a cabeça da lista

    def print(self):
        # Exibe todos os valores da lista, do primeiro ao último nó.
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def remove(self, n):
        # Remove todas as ocorrências do valor 'n' da lista.
        # Primeiro, remove as ocorrências no início da lista.
        while self.head and self.head.value == n:
            self.head = self.head.next

        # Depois, percorre a lista removendo as ocorrências no meio ou no final.
        current = self.head
        while current and current.next:
            if current.next.value == n:
                current.next = current.next.next  # Pula o nó com valor 'n'
            else:
                current = current.next  # Avança para o próximo nó

        return self  # Retorna a lista atualizada

    def split(self, n):
        # Divide a lista em duas a partir da primeira ocorrência do valor 'n'.
        # Retorna a segunda parte da lista, enquanto a lista original é cortada no nó 'n'.
        current = self.head
        while current:
            if current.value == n:
                second_list = Linked_list()
                second_list.head = current.next
                current.next = None
                return second_list
            current = current.next
        return None

    def reverse(self):
        # Inverte a ordem dos nós da lista.
        # O último nó se torna o primeiro, e os ponteiros são ajustados para refletir a nova ordem.
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self

    def equals(self, other_list):
        # Compara duas listas para verificar se são iguais.
        # Retorna True se ambas as listas tiverem os mesmos valores na mesma ordem, caso contrário, False.
        current1 = self.head
        current2 = other_list.head
        while current1 and current2:
            if current1.value != current2.value:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

    def copy(self):
        # Cria uma cópia da lista original.
        # Retorna uma nova lista com os mesmos valores da lista original, mas com nós independentes.
        new_list = Linked_list()
        current = self.head
        while current:
            new_list.insert(current.value)
            current = current.next
        return new_list

    def insert_circular(self, value):
        # Insere um novo nó com o valor especificado em uma lista circular.
        # Se a lista estiver vazia, o novo nó aponta para si mesmo. Caso contrário, é inserido após a cabeça.
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        return self

    def remove_circular(self, value):
        # Remove o nó com o valor especificado de uma lista circular.
        # Se o valor estiver na cabeça, a cabeça é atualizada. Se a lista ficar vazia, a cabeça é definida como None.
        if not self.head:
            return self

        current = self.head
        while current.next != self.head:
            if current.next.value == value:
                current.next = current.next.next
                return self
            current = current.next

        if self.head.value == value:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head.next = self.head.next.next
                self.head = self.head.next

        return self

def merge(l1, l2):
    # Intercala duas listas ordenadas em uma nova lista.
    # Retorna uma lista com os nós de ambas as listas, mantendo a ordem crescente.
    merged_list = Linked_list()
    current1 = l1.head
    current2 = l2.head

    while current1 and current2:
        if current1.value < current2.value:
            merged_list.insert(current1.value)
            current1 = current1.next
        else:
            merged_list.insert(current2.value)
            current2 = current2.next

    while current1:
        merged_list.insert(current1.value)
        current1 = current1.next

    while current2:
        merged_list.insert(current2.value)
        current2 = current2.next

    return merged_list

# Teste das funções
if __name__ == "__main__":
    # Criando e testando a lista original
    node = Linked_list()
    node.insert(69)
    node.insert(88)
    node.insert(101)
    node.insert(920)
    node.insert(88)
    node.insert(920)
    node.insert(55)
    node.insert(6)
    node.insert(9)

    print("Original list:")
    node.print()

    # Teste da função remove
    node.remove(920)
    print("\nList after removing 920:")
    node.print()

    # Teste da função split
    lista2 = node.split(88)
    print("\nList after splitting at value 88:")
    node.print()
    print("Split list:")
    lista2.print()

    # Teste da função merge
    lista3 = Linked_list()
    lista3.insert(100)
    lista3.insert(200)
    lista3.insert(300)

    merged = merge(node, lista3)
    print("\nMerged list:")
    merged.print()

    # Teste da função reverse
    reversed_list = merged.reverse()
    print("\nReversed list:")
    reversed_list.print()

    # Teste da função equals
    print("\nIs the original list equal to the reversed list?", node.equals(reversed_list))

    # Teste da função copy
    copied_list = node.copy()
    print("\nCopy of the original list:")
    copied_list.print()

    # Teste da lista circular
    circular = Linked_list()
    circular.insert_circular(100)
    circular.insert_circular(200)
    circular.insert_circular(300)
    print("\nCircular list (cannot be printed with the normal print function):")
    # Para imprimir uma lista circular, você precisaria de uma função específica.