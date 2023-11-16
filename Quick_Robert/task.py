import os 
import random 
import string 
import hashlib 
from Crypto.Util.number import getPrime  
from gmpy2 import legendre 
flag = os.environ.get("FLAG", b"SYC{Al3XEI_FAKE_FLAG}")
DEBUG = True 
banner = '|'*70

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

def gen1(nbits):
    while True: 
        p = getPrime(nbits) 
        b = random.getrandbits(nbits) 
        k = random.getrandbits(10) 
        _4ac = k*p-b**2
        if _4ac%4 == 0:
            c = 1
            a = _4ac//(-4)
            break 
    assert (b**2-4*a*c)%p==0
    a = random.randint(a-1,a+1)  
    return (p,a,b,c) 

def s1(set): 
    p,a,b,c = set 
    if (b**2-4*a*c)%p !=0:
        return -legendre(a,p) 
    else:
        return legendre(a,p)*(p-1) 


try:
    proof_of_work() 
    print(banner) 
    print('\nHi Crypto-ers! AL3XEI Here. In number theory, if there exists an integer q satisfying x^2=q(mod n), q is so called a quadratic residue.')  
    print('We write this calculation as L(a,p), which its value shows a is or is not quadratic residue modulo p.') 
    print('if p|a, L(a,p)=0; if a is a quadratic residue modulo p, L(a,p)=1; if a is not, L(a,p)=-1.')
    print('Below, you need to give me the answer of the sum of L(a*l**2+b*l+1,p), where a,b are integers, p is a prime, and l rise from 0 to p-1.')
    print('For example, given a = 2, b = 3, c = 1, p = 5, the answer will be L(1, 5) + L(6, 5) + L(15, 5) + L(28, 5) + L(45, 5) = 1.')
    print('Hope you success!\n') 
    print(banner+'\n') 

    for i in range(10): 
        nbits = random.randint(1000,1024)
        set = gen1(nbits)   
        p,a,b,c = set 
        print("{} * l**2 + {} * l + {}".format(a,b,c))
        print("p = {} ({} bits)".format(p,nbits)) 
        ans = s1(set) 
        if DEBUG:
            print("ans = ", ans) 
        res = int(input("\n> Type your answer: "))  
        if res == ans:
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
