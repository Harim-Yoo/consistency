import sympy as sp 
import math 

a = sp.Symbol("a",integer=True)
b = sp.Symbol("b",integer=True)
c = sp.Symbol("c",integer=True)

def heron(a,b,c):
    s = (a+b+c)/2
    return math.isqrt(int(s*(s-a)*(s-b)*(s-c)))
    
result = heron(16,30,34)
print(result)
