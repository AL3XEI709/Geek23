import random
from Crypto.Util.number import * 
import gmpy2 as gp 

class ntru():

    def gen(self,bound):
        q=getPrime(bound)
        bound1=int(gp.iroot(q//2,2)[0])
        bound2=int(gp.iroot(q//4,2)[0])
        while True:
            f,g=random.randint(1,bound1),random.randint(bound2,bound1)
            if gp.gcd(f,q*g) == 1 :
                break 
        h=(gp.invert(f,q)*g)%q
        return int(q),int(h),f,g 

    def enc(self,m,bound,q,h):
        m_=long_to_bytes(m)
        assert m_<gp.iroot(bound//4,2)[0]
        r=getPrime(bound//2)
        e=(r*h+m)%q
        return e

    def dec(self,e,f,g,q):
        a=f*e%q 
        b=gp.invert(f,g)*a%g 
        return b 
    
s = ntru() 
set = s.gen(128)
print(set) 