class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp_head = self.head
        while temp_head != None:
            print(f'{temp_head.data}-->',end='')
            temp_head = temp_head.next

    def add_start(self, data):
        node = Node(data)#new
        node.next = self.head
        self.head = node

    def add_end(self, data):
        temp_head = self.head
        while temp_head.next != None:
            temp_head = temp_head.next
        node = Node(data)
        temp_head.next = node

    def add_before(self, data, target_data):
        #adding before node 1
        if self.head == None:
            print('linked list is empty')
            return
        if self.head.data == target_data:
            self.add_start(data=data)
            return
        #adding before node 3
        temp_head = self.head
        while temp_head.next != None:
            if temp_head.next.data == target_data:
                break
            temp_head = temp_head.next
        node = Node(data=data)
        node.next = temp_head.next
        temp_head.next = node

    def remove_start(self):
        if self.head == None:
            print('Linked List is empty')
            return
        self.head = self.head.next

    def remove_middle(self, target_data):
        temp_head = self.head
        while temp_head.next != None:
            if temp_head.next.data == target_data:
                break
            temp_head = temp_head.next
        else:
            print(f'Target {target_data} does not exist')
            return
        temp_head.next = temp_head.next.next

    def remove_end(self):
        if self.head == None:
            print('Linked List is empty')
            return
        temp_head = self.head
        while temp_head.next.next != None:
            temp_head = temp_head.next
        temp_head.next = None

        
link = LinkedList()
link.add_start(10)
link.add_end(20)
link.add_end(30)
link.add_before(25, 10)
link.add_before(50, 25)
link.add_before(90, 30)
link.add_before('David', 10)
link.remove_end()
link.remove_end()

link.traverse()



