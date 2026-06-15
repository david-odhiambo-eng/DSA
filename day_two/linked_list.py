class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        n = self.head
        if n == None:
            print('List is empty')
        else:
            while n != None:
                print(f'{n.data}-->',end='')
                n = self.head.link

    def add_start(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            node.link = None
        else:
            node.link = self.head
            self.head = node

    def add_end(self, data):
        n = self.head
        if n == None:
            self.add_start(data)
        else:
            while n != None:
                self.head = self.head.link
            node = Node(data)
            self.head = node
            node.link = None
            

            
        node = Node(data)

link = LinkedList()
link.add_start(34)
link.add_start(55)
link.add_start(101)
link.add_end(250)
link.add_end(20)
link.add_end(45)
link.traverse()

            

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.link = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def traverse(self):
#         if self.head == None:
#             print('List is empty')
#         else:
#             n = self.head
#             #we use while if we know the stopping condition
#             while n != None:
#                 print(n.data,end='-->')
#                 n = n.link

#     def add_start(self, data):
#         #We first create a node
#         #By default, a created node has data and link None
#         node1 = Node(data)
#         #since the link is null, we point it to the head, which stores a reference to the initial first node
#         node1.link = self.head
#         #we then change the head to point to the added node
#         self.head = node1# now head reads the location that was assigned during creating node

# link = LinkedList()
# link.add_start(34)
# link.traverse()





