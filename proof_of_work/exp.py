from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 

table = string.ascii_letters+string.digits


tail,h = b"HF9KuMrgxUrJMKlT",b"5ed2d32f77c2e0c532ed0836ef8623e388828ade827841670c329072c8fe4dac"
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print("".join(head))  
        exit()
