for a in range(1,10):
    for b in range(10,100):
        for c in range(10,100):
            x = int(str(a)+str(b)+str(c))
            if x == (a+b+c)**3:
                print((a,b,c))

------------------------------------------------
