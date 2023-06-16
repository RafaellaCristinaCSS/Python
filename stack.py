# A Stack suporta as seguintes operações padrão:

# push: Empurra um item para o topo da Stack.
# pop: Remova e devolva o item do topo da Stack.
# peek: Retorna o item no topo da Stack sem removê-lo.
# size: Retorna o número total de itens na Stack.
# isEmpty: Verifica se a Stack está vazia.
# isFull: Verifica se a Stack está cheia.


# Implementação de Stack usando uma lista
# A Stack pode ser facilmente implementada como uma lista. A seguir está a implementação de Stack personalizada em Python, que usa uma lista:

# Implementação de Stack personalizada # em Python
class Stack:
 
    # Construtor # para inicializar a Stack
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1
 
    # Função para adicionar um elemento `val` à Stack
    def push(self, val):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)
 
        print(f'Inserting {val} into the stack…')
        self.top = self.top + 1
        self.arr[self.top] = val
 
    # Função para remover um elemento superior da Stack
    def pop(self):
        # verifica se há underflow da Stack
        if self.isEmpty():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)
 
        print(f'Removing {self.peek()} from the stack')
 
        # diminui o tamanho da Stack em 1 e (opcionalmente) retorna o elemento estourado
        top = self.arr[self.top]
        self.top = self.top - 1
        return top
 
    # Função para retornar o elemento do topo da Stack
    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.arr[self.top]
 
    # Função para retornar o tamanho da Stack
    def size(self):
        return self.top + 1
 
    # Função para verificar se a Stack está vazia ou não
    def isEmpty(self):
        return self.size() == 0
 
    # Função para verificar se a Stack está cheia ou não
    def isFull(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    stack = Stack(3)
 
    stack.push(1)       # Inserindo 1 na Stack
    stack.push(2)       # Inserindo 2 na Stack
 
    stack.pop()         # removendo o elemento superior (2)
    stack.pop()         # removendo o elemento superior (1)
 
    stack.push(3)       # Inserindo 3 na Stack
 
    print('Top element is', stack.peek())
    print('The stack size is', stack.size())
 
    stack.pop()         # removendo o elemento superior (3)
 
    # verifica se a Stack está vazia
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')
