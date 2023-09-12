class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insertFirst(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
            
        
        
LL = LinkedList()
LL.insertFirst(2)
LL.insertFirst(3)
        