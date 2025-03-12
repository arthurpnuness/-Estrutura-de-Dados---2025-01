
class Node:
    def __init__   (self, value): ## __init__ cria um novo nó 
        self.value = value ## Armazena o numero do nó 
        self.next = None ## Ponteiro inicialmente nao aponta para nada (NONE), porque ainda nao sabemos o prox

class Linked_list:
    def __init__(self):
        self.head = None ## Aqui guardamos a referencia do primeiro nó da lista

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node ## Novo nó se torna a cabeça da lista

    def print(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("none")
    
def remove(list, n):
    ## Aqui vamos remover todas as ocorrencias de 'n' no inicio
    while list.head and list.head.value == n:
        list.head = list.head.next
        
    ## Vamos percorrer a lista removendo ocorrencias
    current = list.head
    while current and current.next:
        if current.next.value == n:
            current.next = current.next.next ## Pula o nó com valor n
        else:
            current = current.next ## Avança para o prox nó
        
    return list #Retorna a lista 

## test

if __name__ == "__main__":
    node = Linked_list()
    node.insert(69)
    node.insert(88)
    node.insert(88)
    node.insert(101)
    node.insert(920)
    node.insert(920)
    node.insert(55)
    node.insert(6)
    node.insert(9)

    print("Original list: :")
    node.print()

    remove(node,920) ## Removendo numeros

    print("\nList after remove:")
    node.print()
    
