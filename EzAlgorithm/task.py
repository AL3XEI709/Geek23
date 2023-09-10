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
    if not proof_of_work():
        exit() 
    parms = [random.randrange(2,2<<32) for _ in range(10)]    
    res = int(input(':> ')) 
    if res >= 2**35:
        exit() 
    cnt = 0  
    for _ in range(10): 
        cnt += pow(res,_)*parms[_]  
    print(cnt) 
    ans = input(':> ') 
    ans = [int(_) for _ in ans.split(",")] 
    
    if ans == parms:
        print('Congrats! Your flag is:',flag)  
    else:
        exit()

except Exception:
    print("Something goes wrong...\n") 
    print(banner+'\n') 
    exit() 