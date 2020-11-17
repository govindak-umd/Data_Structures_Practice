class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Adding elements to the front of the list
    def insertFront(self, new_node):
        new_node_front = Node(new_node)
        if self.head is None:
            self.head = new_node_front
            self.tail = new_node_front
        else:
            new_node_front.next = self.head
            self.head.prev = new_node_front
            self.head = new_node_front

    def insertBack(self, new_node):
        new_node_back = Node(new_node)
        if self.head is None:
            self.head = new_node_back
            self.tail = new_node_back
        else:
            self.tail.next = new_node_back
            new_node_back.prev = self.tail
            self.tail = new_node_back

    # Adding elements to the rear of the list
    def printDll(self):
        temp_iterator = self.head

        if self.head is None:
            print('Nothing here')
        while temp_iterator is not None:
            print(temp_iterator.data)
            temp_iterator = temp_iterator.next


if __name__ == '__main__':
    # Initializing the list
    doubly_linked_list = DoublyLinkedList()
    # Adding elements to the front of the list
    doubly_linked_list.insertFront(5)
    doubly_linked_list.insertFront(8)
    doubly_linked_list.insertFront(10)
    # Adding elements to the rear of the list
    doubly_linked_list.insertBack(11)
    doubly_linked_list.insertBack(99)
    # Printing the list
    doubly_linked_list.printDll()
