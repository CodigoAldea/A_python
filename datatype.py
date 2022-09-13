'''
    5 type of data : 
        1. Numeric : int, float, complex ( x + yi)
        2. Boolean
        3. Set
        4. Sequence : List, Tuple, String
        5. Dictionary
        
        
    Set: 
        1. unordered 
        2. iterable 
        3. mutable 
        4. all the elements are unique
    syntax : var_name = {v1, v2, v3 ....}
            a = {1,2,3,4,5}
    
    List : 
        syntax : var_name = [v1, v2,v3.....]
        1. ordered
        2. Arbitrary Objects
        3. Index
            a. positive
            b. negetive 
            c. Slicing 
        4. nested
        5. Mutable 
    
    Tuples:
        Syntax : var_name = (v1,v2 ,v3 ....)
        1. ordered 
        2. immutable
        3. Index
            a. positive
            b. negetive 
            c. Slicing 
        4. Assignment, Packing and Unpacking
        
    String: 
        syntax: var_name = "string"   we can use both " or ' .
        str() : to convert in string
        len() : to check the number of characters or elements
        ord() : convers a char into an int.
        f-string : Formatted string 
            syntax : f'string chars {l} string chars'
        Immutable.
        replace() : to replace a char with another
        join() : conver a list to string. 
        split() : converts string to list.
        byte object : 
            a = b'string'
    
    Dictionaries : 
        Syntax : var = {key:value , key:value, key:value ....}
            key can never be a list or another dictionary
        
        mutable 
        dynamic
        nested
'''
d = {
    'name':'Python',
    "dob":'00000',
    "email":"abc@abc.com"     
    }
d1 = { "dob":'88888',
    "email":"xyz@abc.com",
    "acb": " 333"}

d.update(d1)
print(d)