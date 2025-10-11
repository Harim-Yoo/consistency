#2016 LMM 17 Wrong Approach
a=1 
b=0 

for i in range(1,20):
    if i%2==1:
        a=a-(1/(i+1))*a
        b=b+(1/(i+1))*a
    elif i%2==0:
        a=a+(1/(i+1))*b 
        b=b-(1/(i+1))*b

print((a,b))
-----------------------------------------------
#After fixing the error

a=1 
b=0 
transfer_amount = 0

for i in range(1,20):
    if i%2==1:
        transfer_amount = 1/(i+1)*a
        a=a-transfer_amount
        b=b+transfer_amount 
    elif i%2==0:
        transfer_amount = 1/(i+1)*b
        a=a+transfer_amount
        b=b-transfer_amount

print((a,b))
