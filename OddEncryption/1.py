from Crypto.Util.number import * 
flag = b"abcdefgh" 
R = bytes_to_long(flag)
mask = 0b1010010000001000000010001001010010100100000010000000100010010100



def lfsr_CopiedfromInternet(R,mask):
    output = (R << 1) & 0xffffffffffffffff
    i = (R & mask) & 0xffffffffffffffff
    lastbit = 0
    while i != 0:
        lastbit ^= (i & 1)
        i = i>>1
    output ^= lastbit
    return (output,lastbit)


res = ""
for i in range(64): 
    (R, out) = lfsr_CopiedfromInternet(R,mask)
    res+=str(out)

print(res)