# WAP generate a random hex 

import random
#import string

c = random.randint(0, 0xFFFFF)

print("#{:06x}".format(c))

# random string 
#d= random.choice(string.ascii_letters)
d= chr(random.randint(ord('a'),ord('z')))
print(d)