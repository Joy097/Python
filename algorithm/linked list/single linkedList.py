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
            
    def insertLast(self,data):
        if self.head:
            itrNode = self.head
            while itrNode:
                itrNode = itrNode.next
            itrNode.next = Node(data,None)
        else:
            
        
    def printlist(self):
        if self.head:
            head = self.head
            string = ''
            while(head):
                string += str(head.data) + '-->'
                head = head.next
        else:
            return "List is empty"
        return string
                
LL = LinkedList()
LL.insertFirst(2)
LL.insertFirst(3)
LL.insertFirst(4)
LL.insertFirst(5)

print(LL.printlist())
        