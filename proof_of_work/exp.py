from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 

table = string.ascii_letters+string.digits


tail,h = b"HF6oo5qN5kUVucEZ",b"1b733be5f9a9777a5fc2e2314f255a441806eb487a02f882d73f1d5419612fce"
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print("".join(head))  
        exit()
