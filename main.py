from typing import Any

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value: Any) -> None:
        node = Node(value, self.head)
        self.head = node

    def append(self, value: Any) -> None:
        if self.head == None:
            self.head = Node(value, None)
            return
        obecny = self.head
        while obecny.next:
            obecny = obecny.next
        obecny.next = Node(value, None)

    def pop(self) -> Any:
        usun = self.head
        self.head = usun.next
        return usun

    def print(self):
        obecny = self.head
        zawartosc = ""
        while obecny:
            zawartosc += str(obecny.value) + " -> "
            obecny = obecny.next
        print(zawartosc)

    def len(self):
        ilosc = 0
        obecny = self.head
        while obecny:
            ilosc += 1
            obecny = obecny.next
        return ilosc

class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.pop().value

    def print(self):
        return self._storage.print()

    def len(self):
        return self._storage.len()

class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def enqueue(self, element: Any) -> None:
        self._storage.push(element)

    def dequeue(self) -> Any:
        self._storage.pop()

    def print(self):
        return self._storage.print()

    def len(self):
        return self._storage.len()

#Zadanie 1
lista = LinkedList()
assert lista.head == None
lista.push(34)
lista.push(65)
lista.push('pies')
lista.append('fiji')
lista.append(23)
lista.print()
print("Ilość elementow w tablicy:", lista.len())
lista.pop()
lista.print()
print("Ilość elementow w tablicy:", lista.len())
print("")

#Zadanie 2
stos = Stack()
assert stos.len() == 0
stos.push(3)
stos.push(8)
stos.push(1)
stos.print()
assert stos.len() == 3
print("Ilość elementow w stosie:", stos.len())
stos.pop()
stos.print()
print("Ilość elementow w stosie:", stos.len())
print("")

#Zadanie 3
kolejka = Queue()
assert kolejka.len() == 0
kolejka.enqueue('klient1')
kolejka.enqueue('klient2')
kolejka.enqueue('klient3')
kolejka.print()
print("Ilość ludzi w kolejce:", kolejka.len())
kolejka.dequeue()
kolejka.print()
print("Ilość ludzi w kolejce:", kolejka.len())