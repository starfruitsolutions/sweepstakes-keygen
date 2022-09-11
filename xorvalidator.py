import string
import hashlib

secret = "somebullshit"
values = ['5', '10', '15', '20']

def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

while True:
    encoded = input("Enter your code: ")

    decoded = str_xor(encoded, secret)
    print(decoded)
    value = decoded[4: ]
    if value in values:
        print('You redeemed ' + value + ' points!')
    else:
        print('Invalid Code')
