from Crypto.Cipher import DES
import os 
from binascii import hexlify as hy, unhexlify as uhy
import random 
import string 
import hashlib 

xor = lambda a,b: bytes([a[i % len(a)] ^ b[i % len(b)] for i in range(max(len(a), len(b)))])
pad = lambda msg,padlen: msg+chr((padlen-(len(msg)%padlen))).encode()*(padlen-(len(msg)%padlen))

flag = os.environ.get("FLAG", b"SYC{Al3XEI_FAKE_FLAG}").encode()
sec = os.urandom(8)

banner = '|'*70


def proof_of_work():
    proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
    digest = hashlib.sha256(proof.encode()).hexdigest()
    print("sha256(XXXX+%s) == %s" % (proof[4:], digest))
    x = input("Give me XXXX: ")
    if len(x)!=4 or hashlib.sha256((x+proof[4:]).encode()).hexdigest() != digest: 
        return False
    print("Right!")
    return True



def enc(msg,key):
    try:
        key = uhy(key) 
        msg = xor(uhy(msg),sec) 
        des = DES.new(key,DES.MODE_ECB) 
        ct = xor(des.encrypt(pad(msg,8)),sec) 
        return hy(ct).decode() 
    except:
        return Exception 

def service():
    cnt = 0
    if not proof_of_work():
        exit()
    print(banner) 
    print('Simple DES Encryption Service')
    print(banner)
    while cnt<2:
        print('1. Encrypt\n2. Get encrypted flag.')
        choice = int(input('> '))
        if choice == 1:
            print('Input msg(hex):') 
            msg = input('> ').strip() 
            print('Input key(hex):')
            key = input('> ').strip()  
            print(enc(msg,key)) 
        elif choice == 2:
            print('Input key(hex):') 
            key = input('> ').strip()   
            print(enc(hy(flag),key)) 
        else:
            exit() 
        cnt+=1
    print(banner)
    print('Bye!')
    exit()

try:
    service() 
except Exception:
    print("Something goes wrong...\n") 
    print(banner+'\n') 
    exit() 



        

