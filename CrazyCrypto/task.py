
import random 
from Crypto.Util.number import *
from tqdm import tqdm 

n = 65537
def count_repeats(a):
    dict = {}
    for key in a:
        dict[key] = dict.get(key, 0) + 1
    for i in sorted (dict) : 
        print ((i, dict[i]), end =" ") 


pts = [] 

for _ in tqdm(range(100000)):
    ps = bin(random.getrandbits(65537)).count('1')
    pts.append(ps) 

xy = count_repeats(pts)
