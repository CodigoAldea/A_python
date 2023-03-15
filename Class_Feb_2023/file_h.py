'''
    3 operations : 
        open  : open() 
        read / write   : read()  / write ()
        close : close()
        
        # to read or write in a file we need to open the file with the 
        specific access mode. 
        
        open() Syntax : 
            var ( file object )= open(file_name, access mode , buffering )
'''



a = open("test.txt", "r")
n=int(input("Enter the number of line : "))
for i in a.readlines()[-n:]: 
    print(i, end='')


"""# for writng in the file : 
a = open("test.txt", "a")
a.write("hello")
a.close()"""