# 1- import string module
# 2- store all caracters in lists (upper/lower case, digists, punctuation)
# 3- take number of charset from user
# 4- make sure the number of characters is 6 or more
# 5- shuffle all lists
# 6- calculate 30% and 20% of number of caracters
# 7- create password  60% letters and 40% digits and punctuation

import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("how many characters for the password?: ")
while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("you need at least 6 characters")
            characters_number = input("please enter the number again: ")
        else:
            break
    except:
        print("please enter the numbers only")
#characters_number = input("how many characters for the password?: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(characters_number * (30 / 100))
part2 = round(characters_number * (20 / 100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part1):
    password.append(s3[i])
    password.append(s4[i])
print(password)

password = "".join(password[0:])

print(password)
