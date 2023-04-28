class mobile:
    def __init__(self,a,b) :
        self.att = a
    def __contains__(self,a) :
        return a in self.att
        
    a='samsung'
    b='2.7GHz'
    c='32GB'
    #def abc(self):
    #    print("hello from function inside a class")
    
obj=mobile('python', 5) 
obj1=mobile('classes', 5)

print('python' in obj)
