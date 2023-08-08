from Crypto.Util.number import * 
import os 
flag = b'xxxxxxxx'

def pad(message,padlen):
    return message+os.urandom(padlen-len(message))


flag = pad(flag,32)
print(len(flag))
p = [getPrime(16) for _ in range(32)] 
c = [bytes_to_long(flag)%i for i in p] 


print('p=',p)
print('c=',c)

'''
p= [58657, 47093, 47963, 41213, 57653, 56923, 41809, 49639, 44417, 38639, 39857, 53609, 55621, 41729, 60497, 44647, 39703, 55117, 44111, 57131, 37747, 63419, 63703, 64007, 46349, 39241, 39313, 44909, 40763, 46727, 34057, 56333]
c= [36086, 4005, 3350, 23179, 34246, 5145, 32490, 16348, 13001, 13628, 7742, 46317, 50824, 23718, 32995, 7640, 10590, 46897, 39245, 16633, 31488, 36547, 42136, 52782, 31929, 34747, 29026, 18748, 6634, 9700, 8126, 5197]
'''
