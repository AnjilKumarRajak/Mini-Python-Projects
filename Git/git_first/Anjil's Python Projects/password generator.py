import string
import random

althogether=string.ascii_letters+string.punctuation+string.digits


password=""
for i in range(0,12):
    password+=random.choice(althogether)

print(password)

