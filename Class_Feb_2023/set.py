'''
    Set : 
        it is unordered 
        
        Syntax : var = { 1, 3, 4,5} 
        
        to access the element we use loop (for)
        
        to convert a datatype into set :  Type casting 
            set()
        
        to add an element to the set: 
            add()
            update() : we use a list with update.
            
        union() : to join two sets  : No concatination 
        intersection() : gives common element from the sets 
        
        How to remove an element from a set : 
            remove()
            discard()
'''
a= {1, 2, 3 ,4 ,5 }
z= {1, 2, 3 ,4 ,5 , 4, 5, 6, 7, 8}
a.discard(5)
print(a)
