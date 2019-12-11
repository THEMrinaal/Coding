class node:
    def __init__(self,data):
        self.data = data
        self.next=None

class LinkedList:

    def __init__(self):
         self.head=None

    def  append(self,data):
        temp = node(data)     #node created with data!
        if self.head is None:
            self.head= temp
            return
        else:

            lastnode= self.head
            while(lastnode.next):
                lastnode= lastnode.next
            lastnode.next= temp
    def show(self):
        itr= self.head
        while(itr):
            print(itr.data)
            itr= itr.next
    def prepend(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
        
