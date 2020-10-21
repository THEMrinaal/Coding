class Node:
  def __init__(self,data=None,next=None):
    self.data= data
    self.next= next
  def setData(self,data):
    self.data=data
  def getData(self):
    return self.data

  def setNext(self,next):
    self.next=next
  def getNext(self):
    return self.next

  def hasNext(self):
    return self.next!=None



class LinkedList(object):
  def __init__(self,node=None):
    self.length=0
    self.head=node


  def length(self):
    l=0
    current= self.head                      # Starting with head!
    while current!=None:
      l=l+1
      current = current.next
    return l
  
  def insertAtbeginning(self,data):
    newNode = Node()
    newNode.data= data

    if self.length==0:
      self.head= newNode
    else:
      newNode.next = self.head
      self.head = newNode

    self.length+=1
  

  def insertx(self,data):
    newNode = Node()
    newNode.data = data

    current = self.head
    while current.next != None:
      current=current.next
    
    current.next = newNode
    self.length+=1

  def insertAtAnyIndex(self,data,pos):
    newNode = Node()
    newNode.data = data
    if pos==0:
      self.head = newNode

    current = self.head
    i=0
    while i<pos-1:
      current = current.next
      i=i+1
    newNode.next = current.next
    current.next = newNode
    self.length+=1

  def deleteFromBeginning(self):
    if self.length ==0:
      print("The LL is empty!")
    else:
      self.head = self.head.next
    self.length-=1

  def deleteFromEnd(self):
    if self.length==0:
      print("LL is empty!")
    current= self.head
    while current.next.next!=None:
      current= current.next
    
    current.next = None
    self.length-=1
  def show(self):
    if self.length==0:
      print("LL is empty")
      return

    current= self.head
    while current!=None:
      print(current.data)
      current=current.next

  def deleteAtPos(self,pos):
    if self.length==0:
      print('LL is empty!')
    i=0
    current= self.head
    previous= None
    while i<pos:
      previous= current
      current= current.next
      i=i+1
    previous.next=current.next
    current.next = None

    
  
ll = LinkedList()
ll.insertAtbeginning(4)
ll.show()
print()
ll.insertx(3)
ll.insertx(2)
ll.insertx(1)
print()
ll.show()
ll.deleteFromBeginning()
print()
ll.show()
