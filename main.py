from replit import db
import os

# store my name in the replit db
#db['name'] = "Robert"

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
    
print(factorial(5))

print(db['name'])

keys = db.keys()

print(keys)

for key in db.keys():
  print(db[key])

myApiKey = os.environ['apiKey']
print(myApiKey)
