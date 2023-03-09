'''
    dictionary : 
        syntax : 
        
        d = {"key": "value"}
        to access the value we will use the key as an index 
        
    to add : 
        var["new_key"] = value
    
    to delete the value:
        del
        
    there are 2 pre defined list : 
        keys() : a list that contains all the keys present in the dict.
        values() : a list that contain all the values in the dict.
'''

d = { 
     "name": "python",
     "id" : 30, 
    }
d["time"] = 4
print(d)
k = d.keys()
print(k)