import string 
abc = string.ascii_lowercase
c = "pqcqqc_m1kt4_njn_5slp0b_lkyacx_gcdy1ud4_g3nv5x0"
k = 'flag' # k+key = c
key = [abc[ord(c[_]) - ord(k[_])] for _ in range(4)] 
print(key)
for _ in range(len(c)):
    if c[_] in abc:
        print(chr(ord(c[_])-key[_%4]),end="") 
    else:
        print(c[_],end="")