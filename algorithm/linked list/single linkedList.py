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
            
    def print(self):
        if(self.head):
            head = self.head
            str = ''
            while(head):
                str = head + '-->'
                head = head.next
        else:
            return "List is empty"
        
                
LL = LinkedList()
LL.insertFirst(2)
LL.insertFirst(3)
LL.insertFirst(4)
LL.insertFirst(5)

LL.print
        