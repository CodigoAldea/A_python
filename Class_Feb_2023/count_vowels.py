a = input("enter a string : ")
b= ('a', 'e', 'i', 'o', 'u')
count = 0
for i in a : 
    if i in b:
        count+=1
print("total number of vowels : ", count)