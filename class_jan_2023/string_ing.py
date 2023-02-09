def st(a):
    if len(a) >=3:
        if a[-3:] == 'ing':
            a+='ly'
        else:
            a+='ing'
        print(a)
    else:
        print("length of string is less than 3")

a = input("enter a string : ")
st(a)