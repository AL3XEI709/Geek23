import gmpy2 as gp 
from Crypto.Util.number import *  
from output import e1,e2,c1,c2,c,n


e = 65537 
t1 = (gp.powmod(c1,e2,n)*gp.powmod(5,e1*e2,n))%n
t2 = (gp.powmod(c2,e1,n)*gp.powmod(2,e1*e2,n) )%n
p = gp.gcd((t1-t2)%n,n)  
assert n%p == 0
q = n//p 
d = gp.invert(e,(p-1)*(q-1)) 
m = gp.powmod(c,d,n) 
print(long_to_bytes(m))
# b"SYC{poly_rsa_Just_need5_s1mple_gcd}"
