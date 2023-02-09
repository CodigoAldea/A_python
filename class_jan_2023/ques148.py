s = [0,1,2,3,4,-5]
a = s[0] # to check the greatest number 
b = s[0] # to chesk the smallest number 

for i in s:
    if i > a:
        a = i
    elif i < b:
        b = i
print("max : ",a, "min: ",b)