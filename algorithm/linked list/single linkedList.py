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
            while itrNode.next:
                itrNode = itrNode.next
            itrNode.next = Node(data,None)
            
        else:
            self.head = Node(data,None)
            
            
    def insertList(self,list):
        for data in list:
            self.insertLast(data)
            
            
    def removeItem(self,index):
        if index<1 or index>self.get_length():
            raise Exception("Invalid index!") 
        
        if index == 1:
            self.head = self.head.next
            return
        
        head = self.head
        count = 1
        while head.next:
            if count == index - 1:
                head.next = head.next.next
                break
            
            head = head.next
            count+=1
            
            
    def insertAt(self,index,val):
        if index<1 or index>self.get_length():
            raise Exception("Invalid index!") 
        
        if index == 1:
            self.insertFirst(val)
            return
            
        head = self.head
        count = 1
        while head.next:
            if count == index - 1:
                head.next = Node(val,head.next)
                break
            
            head = head.next
            count+=1
        
    
    def printlist(self):
        if self.head:
            head = self.head
            string = ''
            while(head):
                string += str(head.data) + ' --> '
                head = head.next
        else:
            return "List is empty"
        return string
    
    
    def get_length(self):
        head = self.head
        count = 1  # beacuse head.next = None will not go to loop but it is the last value
        while head.next:
            count+=1
            head = head.next
        return count
            
            
                
LL = LinkedList()
LL.insertFirst(2)
LL.insertFirst(3)
LL.insertFirst(4)
LL.insertFirst(5)
LL.insertLast(6)
LL.insertList([3,7,9,0])
LL.removeItem(6)
LL.insertAt(4,18)
print(LL.printlist())
print(LL.get_length())
        