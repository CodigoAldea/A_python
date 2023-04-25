class mobile:
    def __init__(self,a,b) :
        self.name=a
        self.id =b
    a='samsung'
    b='2.7GHz'
    c='32GB'
    def abc(self):
        print("hello from function inside a class")
    
obj=mobile('python', 5) 
obj1=mobile('classes', 5)

print(obj.name)
