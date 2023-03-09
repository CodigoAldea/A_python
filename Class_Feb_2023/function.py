'''
    Functions : 
        A collection of statement that work together to perform 
        a specific operation.
        
        type : 
            pre defined 
            user defined
            
        syntax :  def function_name(parameters):
'''
# function definition with parameters
def add(**kargs_a):
    global a 
    for i in kargs_a:
        a += i
    #print("sum : ", a)
    return a

#b = int(input("Enter a number :"))
#c = int(input("Enter a number :"))

x = add(i='4')  # function call

print("sum : ",x)