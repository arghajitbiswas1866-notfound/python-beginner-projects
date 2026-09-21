# Day   project
# 4     Password Generator 

import random

n = int(input("Enter the length of password you want to generate:"))
r = []
for i in range(n):
    item = "abcdefghijklmnopqrstuvwxyzZ1234567890!@#$%^&"
    x = random.choice(item)
    r.append(x)
pd = "".join(r)
print("Your generated password is:",pd)