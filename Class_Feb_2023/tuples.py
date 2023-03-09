'''
    tuple : 
        syntax : 
            var= (ele1, ele2 .... )
        
        it is immutable , no changes once made.
        it is ordered.
        concept of packing and unpacking 
        
        to delete the tuple : 
            del
            
        to count the specific occurence of an element : 
            count()
            Syntax : var = tuple . count(element )
'''

a = (1,2,3,3,4)
b= () # is an empty tuple 

#c , d , e, f = a  # unpacking 
#print(d)
h = a.count(3)
print(h)