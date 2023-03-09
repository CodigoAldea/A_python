def last_e(n):
    return n[-1]

a =[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

b= sorted(a,key =last_e)

print(b)