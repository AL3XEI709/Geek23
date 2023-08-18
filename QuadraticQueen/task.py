def legendre(a,p):
    return pow(a,(p-1)//2,p) 

# p = 104453849128357066949782947372113614291785149886576912977748109352699419129858461629240087864191545181360419716179398972553494694049096244069942778899460986221783983196384168179129084618519496671748167356503587227539058668674963140835506628452735537402608128664573455422978662624629728857668109561263565449919 
p = 127 
flag = b"SYC{H4ll0_L3g4ndr3_H4ll0_J4c0b1}" 
flag = int.from_bytes(flag) 


def enc(n,c,k): 
    res = 0 
    for l in range(0,p):
        res += legendre(l**n+c,p)
        res *=l**k 
    return res 

