a = input ("enter a number : ") # this step take the user input and store the value in variable a 
b = 0 # this is the variable we are using to store the sum hence assigning the value 0 to it to make it int
for i in a: # here we are reating the string stored in a, element wise 
    b=b+int(i) # adding the values or digits from a in b by converting the value to int
print(b) # to provide the output of the final sum .