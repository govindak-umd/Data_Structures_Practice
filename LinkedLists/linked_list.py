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

    linked_list_object.PrintLinkedList()