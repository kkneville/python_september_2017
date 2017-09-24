class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None
        
    def __str__(self):
        return str(self.value)

class Stack(object):
    def __init__(self):
        self.top=None
        self.length=0
        
    def top(self):
        return self.top
    def push(self, val):
        self.length +=1
        node = new Node(val)
        node.next=self.top
        self.top=node
        
    def pop(self):
        if self.top == None:
            return None
        self.length -= 1
        node = self.top
        self.top = node.next
        node.next = None
        return node
    def isEmpty(self):
        return True if self.top == None else False    
    
	
    # def __len__(self):
        # return self.length
    # def __str__(self):
        # pass
    # def __repr__(self):
        # pass #representation
    # def __iter__(self):
        # pass
    # def __next__(self):
        # pass
   # def next = __next__
    #python 2.5 compatibility    
    # def __eq__(self):
        # pass #==
    # def __ne__(self):
        # pass #!=