from math import factorial

def pase(n):

    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(i-j)*factorial(j)),end=" ")
        print() # generating a new line 
    
a = int(input("Enter a number : "))
pase(a)