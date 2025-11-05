n = int(input())
res = []
for _ in range(n):
    val = list(map(int,input().split()))
    res.append(val)

dp = []
for i in range(1,n+1):
    dp.append([0]*i)

dp[0][0] = res[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]+res[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + res[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+res[i][j]

print(max(dp[n-1]))
