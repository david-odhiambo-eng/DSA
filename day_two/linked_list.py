class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        head = self.head
        if head == None:
            print('Linked List is empty')
        else:
            while True:
                print(f'{head.data}--->', end='')
                head = head.next
                if head == None:
                    break
            return head

    def add_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_btwn(self, data, position):
        ...

    # def add_end(self, data):
    #     if self.head == None:
    #         node = Node(data)
    #         self.head = node

    #     else:
    #         head = self.head
    #         while True:
    #             head = head.next
    #             if head == None:
    #                 node = Node(data)
    #                 head = node
    #                 break
                

            
        
        
        
            
        

    

node1 = Node(10)
node2 = Node(44)
node3 = Node('Jesse')
node4 = Node(103)
node5 = Node(1024)
link = LinkedList()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
link.head = node1
link.add_start(31)
link.add_start('Test')
link.add_end(13)
link.traverse()




