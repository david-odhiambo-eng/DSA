class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head == None:
            print('List is empty')
        else:
            n = self.head
            while n != None:
                print(f'{n.data}-->',end='')
                n = n.link

    def add_start(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            node.link = None
        else:
            node.link = self.head
            self.head = node

    def add_end(self, data):
        if self.head == None:
            self.add_start(data)
        else:
            n = self.head
            while n.link != None:
                n = n.link
            node = Node(data)
            n.link = node
            node.link = None

    def add_between(self, data, value):
        n = self.head
        while n.data != value:
            n = n.link
            if n.data == value:
                break
        if n.data == None:
            print('Not found')
        else:
            node = Node(data)
            node.link = n
            n = node


node1 = LinkedList()
node1.add_start(10)
node1.add_end(100)
node1.add_start(30)
node1.add_between(219,2)
node1.traverse()
            