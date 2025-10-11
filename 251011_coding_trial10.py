------------------------------------------------------------
3^5=3^{101_2}=3^4\cdot 3^1
result = 1 
5%2==1 --> 101_2의 units digit 1
result = 1*3 % mod
base = 3*3 = 9 --> 다음것 준비
exp // 2 = 2

2%2==0 --> 101_2의 tens digit 0
result는 그냥 패스
base = 9*9=81 --> 다음것 준비
exp // 2 = 1

1%2 == 1 --> 101_2의 hundreds digit 1
result = 3*81 % mod
base = 81*81 --> 다음것 준비
exp // 2 = 0 멈춰!
-----------------------------------------------------------

def modular_pow(base,exp,mod):
    if mod<=0:
        raise ValueError
    result = 1
    while exp>0:
        if exp%2 == 1:
            result = (result*base) % mod
        base = (base*base) %mod
        exp = exp //2 
    return result

e = modular_pow(17,17,6)
print(modular_pow(17,e,7))
