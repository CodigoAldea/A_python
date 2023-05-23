# In Decorators, functions are passed as an argument into 
# another function and then called inside the wrapper function

def abc (a):
    print(a)
    
def xc(func):  # decorator
    func("py")  # abc(a)
    
xc(abc)