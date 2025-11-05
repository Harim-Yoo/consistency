graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(x):
    visited[x] = True 
    for nxt in graph[x]:
        if not (visited[nxt] = True):
            dfs(nxt)

count = 0
for node in range(1,N+1):
    if not (visited[node] = True):
        dfs(node)
        count += 1 
