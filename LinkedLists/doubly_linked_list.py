import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insertFront(self, new_node):
        new_node_front = Node(new_node)
        if self.head is None:
            self.head = new_node_front
            self.tail = new_node_front
        else:
            new_node_front.next = self.head
            self.head.prev = new_node_front
            self.head = new_node_front

    def printDll(self):
        temp_iterator = self.head
        while temp_iterator is True:
            print(temp_iterator.data)
            temp_iterator = temp_iterator.next


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.insertFront(5)
    doubly_linked_list.insertFront(8)
    doubly_linked_list.insertFront(10)
    doubly_linked_list.printDll()
