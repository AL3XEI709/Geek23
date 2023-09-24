from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 

table = string.ascii_letters+string.digits


tail,h = b"LZ6cH3A7FLIN5oSv",b"3fd52369868b6fdc59aaa091836b50ce8bc392984a18d50dc91cbe5c4e41ea3a"
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print("".join(head))  
        exit()
