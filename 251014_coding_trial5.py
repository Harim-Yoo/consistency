numbs = [1,2,3,4]

def f(start, path):
    if len(path)==2:
        print(path)
        return None
    for i in range(start,len(numbs)):
        path.append(numbs[i])
        f(i+1,path)
        path.pop()

f(0,[])
