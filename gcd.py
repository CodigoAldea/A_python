import math
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))

g = math.gcd(a,b)

lcm = (a*b)/g
print("LCM= ", int(lcm))