# assertion 
# syntax : 
#   assert expression [argument]

def sq(a):
    assert (a<0), "give a positive number"
    return a**2
    
print(sq(9))
print(sq(-9))