import random
import string

password = ""
length = int(input("Input length of your password "))
for i in range(length):
  position = random.randint(0,len(string.printable)-1)
  password = password + string.printable[position]
print(password)