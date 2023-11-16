from gmpy2 import legendre,gcd  
from random import randint
from Crypto.Util.number import getPrime 

def gen():
    a,b,c = [randint(0,100) for _ in "abc"] 
    p = getPrime(7) 
    return a,b,c,p 

def s1(a,b,c,p):
    cnt = 0
    for l in range(0,p):
        print(a*l**2+b*l+c,p,legendre(a*l**2+b*l+c,p) )
        cnt += legendre(a*l**2+b*l+c,p) 
    return cnt 

def s2(a,b,c,p):
    if (b**2-4*a*c)%p != 0:
        return -legendre(a,p) 
    return legendre(a,p)(p-1) 

print(s1(2,3,1,5))
print(s2(2,3,1,5)) 