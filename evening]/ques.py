s = input("Enter the string : ")
d={}
for i in s:
    k=d.keys()
    if i in k:
        d[i]+=1
    else:
        d[i]=1
# done with the logic of calculating the repetition 
key = list(d.keys())
val =list(d.values())
l=[]
for i in range(len(key)): # using index
    l.append(str(key[i]))
    l.append(str(val[i]))

print("".join(l))