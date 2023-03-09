a = input("enter the string : ")
b = input("enter the character : ")

i = a.index(b)
print("Before the char : ", a[:i])
print("After the char :", a[i:])