from collections import OrderedDict

s = input("Enter the string : ")
d=OrderedDict.fromkeys(s,0)
for i in s : 
    d[i]+=1
out_s=""
print("final Dictionary :",d)
print("d.items :", d.items())
for a,b in d.items():
    out_s=out_s+a+str(b)

print(out_s)