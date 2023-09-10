import os 
import random 
import string 
import hashlib 
from Crypto.Util.number import * 

flag = os.environ.get("FLAG", b"SYC{Al3XEI_FAKE_FLAG}")
DEBUG = False 
banner = '|'*70
if DEBUG:
    print("==DEBUG MODE==") 

def proof_of_work(): 
    if DEBUG:
        return True
    proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
    digest = hashlib.sha256(proof.encode()).hexdigest()
    print("sha256(XXXX+%s) == %s" % (proof[4:], digest))
    x = input("Give me XXXX: ")
    if len(x)!=4 or hashlib.sha256((x+proof[4:]).encode()).hexdigest() != digest: 
        return False
    print("Right!")
    return True  


def gen(nbits): 
    return [getPrime(nbits) for _ in range(7)] 

def check(ps,ms):
    for _ in ms:
        if _ == 0:
            return False 
    return sum(ps[i]*ms[i] for i in range(7)) 

try:
    r = 15
    if DEBUG:
        r = 1
    if not proof_of_work():
        exit() 
    print(banner)  
    print("\nHi Crypto-ers! AL3XEI here. Solving extended gcd over 2 primes can be easy, but what about 7 primes?") 
    for _ in range(r): 
        nbits = random.randrange(100,200) 
        ps = gen(nbits) 
        print("primes : {} ( {} bits )".format(ps,nbits)) 
        ans = input("Give me a0,...a5,a6: ") 
        ans = [int(i) for i in ans.split(",")] 
        if check(ps,ans):
            print("Good! Next challenge->\n") 
            print(banner+'\n') 
            continue 
        else:
            print("Something goes wrong...\n") 
            print(banner+'\n') 
            exit() 
    print('Congrats! Your flag is:',flag)

except Exception:
    print("Something goes wrong...\n") 
    print(banner+'\n') 
    exit() 