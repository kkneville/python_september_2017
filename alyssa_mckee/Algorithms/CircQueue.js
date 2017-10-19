building on repl.it

latest repl.it version: https://repl.it/L1DJ/22

class CirQueue(object):
  def __init__(self, size):
    self.head = 0
    self.tail = 0
    self.list = [None]*size
    self.size = size
  
  def __str__(self):
    return str(self.list)
    
  def nextIndex(self, i):
    i+=1
    return 0 if i==self.size else i
  
  def isEmpty(self):
    if self.head == self.tail and self.list[self.head] == None:
      return True
    return False
  
  def nextEmpty(self):
    i = self.head
    while(i != self.tail):
      if self.list[i]==None:
        return i
      i = self.nextIndex(i)
    return -1
    
  def enqueue(self, val):
    if self.isEmpty():
      print("enque at empty")
      self.list[self.head] = val
      return
    nextE = self.nextEmpty()
    if nextE != -1:
      print("placed at next empty")
      self.list[nextE] = val
      return
    print("enqueue at tail")
    self.tail = self.nextIndex(self.tail)
    self.list[self.tail] = val
    if self.head == self.tail:
      self.head = self.nextIndex(self.head)
  
  def dequeue(self):
    if self.isEmpty():
      return None
    temp = self.list[self.head]
    self.list[self.head] = None
    if self.head != self.tail:
      self.head = self.nextIndex(self.head)
    return temp
    
  def contains(self, val):
    i = self.head
    while(i != self.tail):
      if self.list[i]==val:
        return True
      i = self.nextIndex(i)
    if self.list[i] == val:
      return True
    return False
 