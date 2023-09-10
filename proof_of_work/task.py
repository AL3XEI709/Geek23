import os 
import random 
import string 
import hashlib 

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

try:
    print("banner") 
    if proof_of_work():
        print('Congrats! Your flag is:',flag) 
    exit() 

except Exception:
    print("Something goes wrong...\n") 
    print(banner+'\n') 
    exit() 