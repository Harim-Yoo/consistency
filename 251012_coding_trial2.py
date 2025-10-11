#  The product of two or more consecutive positive integers is 47AB74; i.e., a 6-digit number beginning 47 and ending 74. List these consecutive integers having the desired product.

answer=[]
for n in range(1,100):
    for k in range(2,10):
        N = 1 
        for i in range(k):
            N *= n+i
        answer.append(N)

actual = []
for x in answer:
    x = str(x)
    if len(x)== 6 and x[:2]=="47" and x[-2:]=="74":
        actual.append(x)

print(actual)
