# 28 = 1 + 2 + 4 + 7 + 14.

def perfect_p(a):
    b = 0 
    for i in range(1,a):
        if a%i==0:
            b+=i
    print(b)
    if b == a:
        print("Perfect number.")
    else:
        print("not a Perfect number.")

x = int(input("enter a number : "))
perfect_p(x)