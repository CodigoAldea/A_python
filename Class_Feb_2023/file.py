def abc():
    s= 'The quick brown fox jumps over the lazy dog'

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in alphabet : 
        if i not in s.lower():
            print("False")
            quit() # it is use to exit the program 
    print("true")
abc()