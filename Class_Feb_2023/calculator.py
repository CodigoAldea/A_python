'''
    To make a simple calculator we need 3 input :
        2 numbers and an operator from user.
'''
a = int(input("Enter the first number : "))
b = int(input("Enter the Second number : "))
c = int(input("Press the 1 for Add, 2 for Sub, 3 for Mul, 4 for Div : "))
# conditions : 
if c == 1 : 
    print("Sum :",a+b)
elif c ==2 : 
    print("Difference : ", a-b)
elif c ==3 : 
    print("Product : ", a*b)
elif c ==4 : 
    print("Division : ", a/b)
else: 
    print("Invalid Choice ! ")