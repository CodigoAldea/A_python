
import re
 
txt = "625,498.002"
x = re.sub(',', 'sub', txt)
print(x)
x = re.sub('\.', ',', x)
print(x)
x = re.sub('sub', '.', x)
print(x)