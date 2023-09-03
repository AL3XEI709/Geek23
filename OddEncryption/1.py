from Crypto.Util.number import *

mask = 0b1010010000001000000010001001010010100100000010000000100010010100

def lfsr_MyCode(R,mask):
    output = (R << 1) & 0xffffffffffffffff
    i = (R ^ mask) & 0xffffffffffffffff
    lastbit = 0
    while i != 0:
        lastbit ^= (i & 1)
        i = i>>1
    output ^= lastbit
    return (output,lastbit)


m = bytes_to_long(b'LFSRsuck') 
R=m
for i in range(35):
    (R, out) = lfsr_MyCode(R,mask) 
print(out) 