#2016 Lehigh Math Meet Recursive Sequence Problem

def f(input):
    result = int(input)
    if result == 0:
        return 0
    elif result%2 == 0:
        return f(result//2) # when dividing integer, use two slashes.
    elif result%2 == 1:
        return f(result//2)+ 1 

print(f(2016))
