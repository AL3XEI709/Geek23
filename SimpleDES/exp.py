from pwn import *
from Crypto.Util.number import long_to_bytes
key = b'FEFEFEFEFEFEFEFE'

rec = remote('59.110.20.54', 23333) 

rec.sendlineafter(b'>',b'2') 
rec.sendlineafter(b'>',key) 
ct = rec.recvline()[1:-1]
rec.sendlineafter(b'>',b'1') 
rec.sendlineafter(b'>',ct) 
rec.sendlineafter(b'>',key)
pt = rec.recvline()[1:-1]
print(long_to_bytes(int(pt,16)))

rec.close()
# b'SYC{DES_1s_0ut_0f_t1me}\xe1\x92z${S\x08\x7fm'