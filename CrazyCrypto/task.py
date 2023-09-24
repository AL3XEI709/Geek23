
import os 
from Crypto.Util.number import *
from tqdm import tqdm 

n = 65537
def count_repeats(args):
    num_count = {}  

    for num in args:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    xy = [] 
    for i in sorted(num_count):
        xy.append([i,num_count[i]]) 
    return xy 


pts = [] 

for _ in tqdm(range(n)):
    ps = bin(bytes_to_long(os.urandom(n//8)))[2:] 
    pts.append(ps.count('1')-ps.count('0'))

xy = count_repeats(pts)
