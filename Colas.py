from abc import ABC, abstractmethod


class Order:
    def __init__(self, qtty: int, customer: str):
        self._customer = customer
        self._qtty = qtty

    def print(self):
        print("     Customer: " + self.get_customer())
        print("     Quantity: " + str(self.get_qtty()))
        print("     ------------")

    def get_qtty(self) -> int:
        return self._qtty

    def get_customer(self) -> str:
        return self._customer


class QueueInterface(ABC):

    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in Queue."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Verifies if the Queue is empty. True if empty | False if not empty."""
        pass

    @abstractmethod
    def front(self):
        """Returns the first element in Queue (not removed). None if empty."""
        pass

    @abstractmethod
    def enqueue(self, info) -> None:
        """Adds a new element to the Queue."""
        pass

    @abstractmethod
    def dequeue(self):
        """Returns the first element in Queue (removed). None if empty."""
        pass


class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next = next_node


class LinkedQueue(QueueInterface):
    def __init__(self):
        self._top = None
        self._last = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._top is None

    def front(self):
        return None if self.is_empty() else self._top.info

    def enqueue(self, info) -> None:
        new_node = Node(info)
        if self.is_empty():
            self._top = new_node
        else:
            self._last.next = new_node
        self._last = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self._top.info
        self._top = self._top.next
        if self._top is None:
            self._last = None
        self._size -= 1
        return info


# Prueba
queue = LinkedQueue()
queue.enqueue(Order(5, "Ana"))
queue.enqueue(Order(2, "Luis"))
queue.enqueue(Order(7, "Marta"))

print(queue.size())
queue.front().print()
queue.dequeue().print()
queue.dequeue().print()
queue.dequeue().print()
print(queue.dequeue())
print(queue.is_empty())