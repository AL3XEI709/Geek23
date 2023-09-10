from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from itertools import product 
import string 

table = string.ascii_letters+string.digits
rec = remote('59.110.20.54', 23333) 


_ = rec.recvuntil(b'XXXX:')

tail,h = _[12:28],_[33:97] 
for head in product(table,repeat=4): 
    m = "".join(head)+tail.decode() 
    h_ = sha256(m.encode()) 
    if h_.hexdigest() == h.decode():
        print('find!') 
        break
rec.sendline("".join(head).encode())

rec.interactive()