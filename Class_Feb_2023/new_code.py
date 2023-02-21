a = [20, 100, 1, 50, 20, 30]
d= {} # empty dict because we need a pair data
for i in a:
    k = d.keys() # list of all the keys 
    if i in k:
        d[i]+=1
    else:
        d[i] = 1
print(d)