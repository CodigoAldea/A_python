a= input("enter the String : ")
b= int(input("Enter the shift number : "))

print("the originar string : ", a)
u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
out=[]
for i in a :  #read the characters from a 
    if i in u: # checking if the character is presrent in u
        z = u.index(i) # getting the index from u
        out+=u[z+b] # adding the shift char to the index 
    elif i in l:
        z = l.index(i)
        out+=l[z+b]
    else:
        print("There is an unknow character in the string .")
print("Caesar Encrypted text : ", "".join(out))