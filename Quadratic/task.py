import gmpy2 
from Crypto.Util.number import *
import tqdm 
l,p,a,b,c = 0,getPrime(2048),5,17,256

res = 0 


if p%(b**2-4*a*c) != 0:
    res_ = -gmpy2.legendre(a,p) 
else:
    res_ = gmpy2.legendre(a,p)*(p-1) 

print(res,res_)
