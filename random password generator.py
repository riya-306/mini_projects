import random
import string
print("enter the maximum length of your desired password - ", )
length = int(input())
values = string.ascii_letters + string.digits + string.punctuation
chars_tt = ""
for i in range(length):
    chars_tt += random.choice(values)
print(chars_tt)