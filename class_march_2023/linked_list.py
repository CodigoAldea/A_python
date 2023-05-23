class node:
    def __init__(self, data):
        self.data = data 
        self.next= None
    
    def __repr__(self) :
        return self.data
        #print(self.data)
    
class list1:
    def __init__(self):  # this is to make the head of the l_list
        self.head = None
    def __repr__(self): # to represent the list in Str format
        a = self.head
        list=[]
        while a is not None:
            list.append(a.data)
            a = a.next
        list.append("None")
        b = "->".join(list)
        #print(b)
        return b
    def __iter__(self):
        a = self.head
        while a is not None:
            yield a
            a = a.next
        
l= list1()
#print(l)
node1 = node("a")
l.head = node1
node2 = node('3')
node1.next = node2
print(l)
for i in l:
    print(i)