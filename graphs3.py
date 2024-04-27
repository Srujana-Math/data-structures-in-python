def storeBFS(startNode, result, adj, n, visited):
    visited[startNode] = True
    Q = [startNode]
 
    while len(Q) > 0:
        currNode = Q.pop(0)
        result.append(currNode)
 
        for neighbour in adj[currNode]:
            if visited[neighbour] == False:
                visited[neighbour] = True
                Q.append(neighbour)
 
def printBFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for i in range(n):
        if visited[i] == False:
            storeBFS(i, result, adj, n, visited)
    print("BFS is:", result)

n, m = map(int, input().split())
adj = []
for i in range(n): 
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
printBFSTraversal(adj, n)
