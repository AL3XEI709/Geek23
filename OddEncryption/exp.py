from sage.all import * 
mask = 322121453779346992541359934248135444081
T1 = matrix(GF(2), 128, 128) 
for i in range(127):
    T1[i, i+1] = 1

T1[-1] = [int(i) for i in bin(mask)[2:]]
E1 = T1 ^ 128
r1 = "11100011101010001100111001010000011010011011010111011111011000110011100010010110110110101001111101101001001010001010001011011010"

b = [int(i) for i in r1] 

ans = E1.solve_right(b) 
print(ans)
flag = 0
for i in ans:
    flag = (flag << 1)+int(i)
print(bytes.fromhex(hex(flag)[2:]))

# b'H4sk3ll_15_C00l!'