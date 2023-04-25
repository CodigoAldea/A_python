# lambda arg : expression 

d = lambda a : a+5

print(d(5))

# map(function, iterable)
'''
l = [1,2,3,4,5,6,7,8]
#p=list(map(lambda a : a*2,l))
p=[i*2 for i in l]
print(p)'''

m = lambda a, b: a if(a>b) else b

print(m(5,6))