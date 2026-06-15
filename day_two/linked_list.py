#Notes on linked list
#A linked list is made up of a node
#A node contains data and a memory address to the next node
#Memory address to the next node can also be called a pointer
#In a list, data is stored in two bytes and every element is arranged next to each other
#This makes insertion and deletion operations at the start and middle of a list to be expensive
#Insertion/deletion involves shifting all other elemenents to occupy the empty position
#This is overcome by linked list as the elements are not arranged next to each other
#A node is made up of 4 bytes, 2 for storing data and 2 for storing the pointer
#the memory locations are scattered all over, with each node having a pointer to the address of the next element

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        #Data is the value that is stored in the a node
        #By default, there is no next node, so we initialize it to None

#creating node objects
node1 = Node(5)
node2 = Node(10)
node3 = Node(-1)
node4 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4
