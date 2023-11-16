import os 
from urllib.parse import unquote 
from base64 import b64decode as dec, b64encode as enc 
from pwn import xor 
import requests
from hashlib import sha512 

def curl_request(url, method='GET', headers=None, data=None):
    try:
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, headers=headers, data=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers, data=data)
        else:
            print("Unsupported HTTP method")
            return None

        # 检查请求是否成功
        response.raise_for_status()

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


f = os.popen('powershell;curl http://localhost:7842').read().split('\n') 
for i in range(len(f)):
    if "Headers" in f[i]:
        f[i], f[i+1], f[i+2], f[i+3] = f[i].strip(), f[i+1].strip(), f[i+2].strip(), f[i+3].strip() 
        x = f[i]+f[i+1]+f[i+2]+f[i+3] 
        break 
x,y = x.split('token') 
token = unquote(y.split(';')[0][1:])  
token = dec(token) 
y,z = y.split('nonce') 
nonce = unquote(z.split(';')[0][1:])  

c1, c2 = token[:len(token)//2], token[len(token)//2:] 
c1 = xor(xor(c1,b'\x10'*16),b'\x1f'*16)

form_data = {
    "Rec": enc(c1+c2).decode()
}
res = curl_request('http://localhost:7842/api/dec', method='POST', headers=None, data=form_data) 
print(res)

for i in range(256):
    form_data = {
        "Password": enc(chr(i).encode()).decode()+enc(sha512(dec(nonce)).digest()).decode()
    }
    res = curl_request('http://localhost:7842/api/check', method='POST', headers=None, data=form_data)
    print(res)
# {"check":"true","msg":"Your flag is: SYC{AL3XEI_FAKE_FLAG}"}