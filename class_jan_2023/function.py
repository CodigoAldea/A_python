'''
    syntax : 
    
    def <name of the function> (parameters):
    
    
    type of arguments :
        1. Default 
        2. keyword
        3. required
        4. variable length :
            *args : we use it for the non-keyword argumnet ; sequence 
            **kwargs: we use it for keyword arguments; dictionary 

'''
#definintion
def add(**kwargs): 
    ''' why are we makeing this function '''
    for i in kwargs.items():
        print(i)
        
add(one= "python", two= "python 2") # one and two are variables 