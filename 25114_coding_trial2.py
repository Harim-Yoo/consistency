#1 연습
def f(a):
    if a == 0:
        return None
    f(a-1)
    print("*"*a)

f(5)

#2 연습 Triangular Number

def triangular_sum(a):
    if a == 1:
        return 1 
    return a + triangular_sum(a-1)

#3 연습 Factorial

def factorial(a):
    if a == 1:
        return 1 
    return a*factorial(a-1)

#4 연습 Fibonacci

def Fibonacci(a):
    if a == 2 or a == 1:
        return 1 
    return Fibonacci(a-1)+Fibonacci(a-2)

