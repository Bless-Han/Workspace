
n, m = map(int, input().split())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, val = map(int, input().split())
    graph[u][v] = graph[v][u] = val
for i in range(1, n + 1):
    graph[i][i] = 0
floyd(graph, n)
ans = float("inf")
for i in range(1, n+1):
    max = 0
    for j in range(1, n+1):
        ...
    if ans > max:
        ans = max
        x = i
if ans == float("inf"):
    print("0")
else:
    print(i, ans)

for v in graph:
    print(v)
