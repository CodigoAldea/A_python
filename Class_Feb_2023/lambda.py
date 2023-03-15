'''Lambda function : 
    syntax : 
        lambda arguments: expression       


a = lambda b: b+9

print(a(5))

it is used with filter() and map(), with if else
statement

'''
# Code to filter odd numbers from a given list  

a=[34, 12, 64, 55, 75, 13, 63]  

o_l=list(filter(lambda x:(x%2!=0),a))

print(o_l)