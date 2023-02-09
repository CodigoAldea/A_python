l = ['a','aa','abc','dddddddd','ffff']
l1=[]
for i in l:
    l1.append((len(i),i))
l1.sort()
print(l1)
print(l1[-1][1])