# WAP to multiply 2 numbers using function : 

# keyword variable-length argument
'''def add(**kargs_a):
    c=0
    for i in kargs_a.values():
        c+=i
    #print(c)
    return c    

b = int(input("Enter a number :"))
a = int(input("Enter a number :"))
d = add(a=1,b=2,c=3,d=4,e=5,f=6)
e = 7 
print(" final answer : ", d+e)'''

#Scope or namespace
def abc():
    a = 1
    #print(a)
    def xyz():
        b=2
        return b
    c = a + xyz()
    return c 
a = abc()
print(a)
