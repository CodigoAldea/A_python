def notpoor(a):
    a_not = a.find("not") # for index of not
    a_p = a.find("poor") # for index of poor
    if a_not < a_p and a_not >0 and a_p >0 :
        a = a.replace(a[a_not:(a_p+4)],'good')
        print(a)
    else:
        print(a)

a = input("enter a sting : ")
notpoor(a)