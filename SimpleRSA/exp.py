import gmpy2
from Crypto.Util.number import * 
from output import p,c

e = 65537 
d = gp.invert(e,p-1)
print(long_to_bytes(gmpy2.powmod(c,d,p))) 
# b'SYC{Just_a_s1mple_modular_equation}'
