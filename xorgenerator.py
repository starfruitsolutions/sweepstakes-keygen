import random
import string

letters = string.ascii_uppercase
values = ['5', '10', '15', '20']
secret = "somebullshit"

def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

for x in range(100):
    ID = ( ''.join(random.choice(letters) for i in range(4)) )
    text = ID + random.choice(values)
    ciphertext = str_xor(text, secret)
    print(ciphertext)
