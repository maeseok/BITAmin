n=int(input())
k=int(input())

visited = [False]*n
graph=[[] for _ in range(n)]
for i in range(k):
     a,b=map(int,input().split())
     graph[a-1].append(b-1)
     graph[b-1].append(a-1)

def dfs(graph, v, visited):
    visited[v]=True
    tmp=0
    for neighbor in graph[v]:
        if not visited[neighbor]:
            tmp+=1
            tmp +=dfs(graph, neighbor, visited)
    return tmp
    
    
answer = dfs(graph, 0, visited)
print(answer)