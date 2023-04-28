import json

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

with open("test.json","w") as t:
    json.dump(thisdict,t)
    
with open("test.json","r") as r:
    t=json.load(r)

print(t)