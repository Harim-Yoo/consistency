#1번 연습

def f(a):
    for i in range(1,a+1):
        print(i)

f(5)

#2번 연습 (recursion)

def f(a):
    if a == 1:
        return None
    f(a-1)
    print(a)
    
f(5)

#3번 연습 (reverse stacking)

def f(a):
    if a == 0:
        return None
    print(a)
    f(a-1)
    
    
f(5)
