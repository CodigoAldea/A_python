def prime(i):
    if (i==1):
        print("Not a prime number.")
    elif (i==2):
        print("Prime number.")
    else:
        for x in range(2,i):
            if(i % x==0):
                print("Not a prime number.")
                break
            print("Prime number.")
            break
    
a = int(input("Enter the number : "))
prime(a)