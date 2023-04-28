import re

# re.match(pattern, string, flags=0)  

line = "Learn Python through tutorials on javatpoint"  
match_object = re.match( r'.w* (.w?) (.w*?)', line)  

print(match_object)