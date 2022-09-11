import string
import hashlib

salt="somebullshit"

while True:
    code = input("Enter your code: ").upper()

    ID = code[0:4]
    checksum = code[4:]

    if(checksum == hashlib.md5((ID + salt).encode()).hexdigest().upper()[ 0 : 4 ]):
        print("validated!")
    else:
        print('Invalid code!')
