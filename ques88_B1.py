a = int(input("Enter a number : "))
sum = 0
for i in range(a,0,-1):
    sum += i**3
print(" Sum of all the cubes for the +ve numbers : ",sum)