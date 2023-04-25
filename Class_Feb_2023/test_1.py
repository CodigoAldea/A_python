class abc:
    def __init__(self, a):  # dunder function
        self.a = a 
    def display(self):
        print(self.a)
    
obj = abc("python")
o2 = abc("coding")
o3 = abc("classes")

o2.display()