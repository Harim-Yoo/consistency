letters = ['E','X','A','M','I','N','E']
letters.sort()
res = []
used = [False]*len(letters)

def dfs(path):
    if len(path)==len(letters):
        res.append(path.copy())
        return None
    for i in range(len(letters)):
        if used[i] == True:
            continue
        if i>0 and letters[i] == letters[i-1] and not used[i-1]:
            continue
        used[i] = True
        path.append(letters[i])
        dfs(path)
        path.pop()
        used[i] = False
dfs([])
print(len(res))
