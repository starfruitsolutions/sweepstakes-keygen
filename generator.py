import random
import string
import hashlib

letters = string.ascii_uppercase
salt="somebullshit"

for x in range(100):
    ID = ( ''.join(random.choice(letters) for i in range(4)) )
    code = ID + hashlib.md5((ID + salt).encode()).hexdigest().upper()[ 0 : 4 ]

    print(code)
