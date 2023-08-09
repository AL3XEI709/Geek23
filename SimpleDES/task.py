from Crypto.Cipher import DES
import os 
from binascii import hexlify as hy, unhexlify as uhy

xor = lambda a,b: bytes([a[i % len(a)] ^ b[i % len(b)] for i in range(max(len(a), len(b)))])
pad = lambda msg,padlen: msg+chr((padlen-(len(msg)%padlen))).encode()*(padlen-(len(msg)%padlen))

flag = os.environ.get("FLAG", b"SYC{Al3XEI_FAKE_FLAG}").encode() 
sec = os.urandom(8)

banner = '|'*70

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

service()




        

