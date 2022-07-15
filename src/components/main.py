import random
import string

password = ""
length = int(input())
for i in range(length):
  position = random.randint(0,len(string.ascii_letters)-1)
  password = password + string.ascii_letters[position]
  
print(password)