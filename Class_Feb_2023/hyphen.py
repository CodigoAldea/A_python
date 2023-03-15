def hyp(s):
    b = s.split("-")
    #print(b)
    b.sort()
    #print(b)
    print("-".join(b))
a= input("Enter the string : ")
hyp(a)