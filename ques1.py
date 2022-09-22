a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

if a % b == 0 : 
    print("GCD = ", b)
else:
    for i in range(int(b/2), 0, -1):
        if a%i == 0 and b%i ==0:
            print("GCD = ", i)
            break