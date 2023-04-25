n = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
a=[]
for i in n:
    a.append(int(abs(i)))

sum=0
for i in a:
    sum+=i

print(sum*len(n))