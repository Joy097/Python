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
            
    def printlist(self):
        if(self.head):
            head = self.head
            str = ''
            while(head):
                str += head.data + '-->'
                head = head.next
        else:
            return "List is empty"
        return str
                
LL = LinkedList()
LL.insertFirst(2)
LL.insertFirst(3)
LL.insertFirst(4)
LL.insertFirst(5)

print(LL.print())
        