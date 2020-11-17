"""
The code demonstrates how to write a code for defining a singly linked list
"""


# Creating a Node Class
class Node:

    # Initialize every node in the LinkedList with a data
    def __init__(self, data):
        # Each of the data will be stored as
        self.data = data
        # This is very important because is links one
        # of the node to the next one and by default
        # it is linked to none
        self.next = None


# Creating a LinkedList class
class LinkedList:

    def __init__(self, ):
        # The below is the head of the LinkedList
        # which is the first element of a LinkedList
        self.head = None

    # Writing a function to print the LinkedList
    def PrintLinkedList(self):
        temporary_head = self.head
        while temporary_head is not None:
            print(temporary_head.data)
            temporary_head = temporary_head.next

    # Implement addition at the beginning functionality
    def addBeginning(self, new_node):
        new_node_beg = Node(new_node)
        new_node_beg.next = self.head
        self.head = new_node_beg

    # Implement addition at the end functionality
    def addEnd(self, new_node):
        new_node_end = Node(new_node)

        # creating a temporary head
        temp_head = self.head

        # keep looping until the head doesn't have anything next
        while temp_head.next:
            temp_head = temp_head.next
        temp_head.next = new_node_end

    # Implement addition at the middle functionality
    def removeNode(self, new_node):
        new_node_removed = Node(new_node)
        temp_head = self.head

        #  removing the first element
        if self.head.data == new_node_removed.data:
            temp_head = temp_head.next
            self.head = temp_head

        #  for removing the any other element other than the first element
        while temp_head.next:
            if temp_head.next.data == new_node:
                temp_head.next = temp_head.next.next
                break
            else:
                temp_head = temp_head.next


if __name__ == '__main__':
    # Creating a LinkedList object
    linked_list_object = LinkedList()
    # Defining the head for the linkedList
    linked_list_object.head = Node(1)
    # defining the second, third and fourth elements in the linked list
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # Linking each element to the next element starting with
    # linking the head to the second element
    linked_list_object.head.next = second
    second.next = third
    third.next = fourth

    # Testing adding in the beginning
    linked_list_object.addBeginning(99)

    # Testing adding at the end
    linked_list_object.addEnd(55)

    # Testing removing any key in the LinkedList
    linked_list_object.removeNode(3)
    linked_list_object.PrintLinkedList()
