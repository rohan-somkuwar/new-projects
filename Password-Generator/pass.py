import random

gen = int(input("Enter the length of Password: "))
s = "ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
p = "".join(random.sample(s,gen))
print(p)