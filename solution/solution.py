"""
7-8 哈利·波特的考试
分数 25
作者 陈越
单位 浙江大学
哈利·波特要考试了，他需要你的帮助。这门课学的是用魔咒将一种动物变成另一种动物的本事。例如将猫变成老鼠的魔咒是haha，将老鼠变成鱼的魔咒是hehe等等。反方向变化的魔咒就是简单地将原来的魔咒倒过来念，例如ahah可以将老鼠变成猫。另外，如果想把猫变成鱼，可以通过念一个直接魔咒lalala，也可以将猫变老鼠、老鼠变鱼的魔咒连起来念：hahahehe。

现在哈利·波特的手里有一本教材，里面列出了所有的变形魔咒和能变的动物。老师允许他自己带一只动物去考场，要考察他把这只动物变成任意一只指定动物的本事。于是他来问你：带什么动物去可以让最难变的那种动物（即该动物变为哈利·波特自己带去的动物所需要的魔咒最长）需要的魔咒最短？例如：如果只有猫、鼠、鱼，则显然哈利·波特应该带鼠去，因为鼠变成另外两种动物都只需要念4个字符；而如果带猫去，则至少需要念6个字符才能把猫变成鱼；同理，带鱼去也不是最好的选择。

输入格式:
输入说明：输入第1行给出两个正整数N (≤100)和M，其中N是考试涉及的动物总数，M是用于直接变形的魔咒条数。为简单起见，我们将动物按1~N编号。随后M行，每行给出了3个正整数，分别是两种动物的编号、以及它们之间变形需要的魔咒的长度(≤100)，数字之间用空格分隔。

输出格式:
输出哈利·波特应该带去考场的动物的编号、以及最长的变形魔咒的长度，中间以空格分隔。如果只带1只动物是不可能完成所有变形要求的，则输出0。如果有若干只动物都可以备选，则输出编号最小的那只。

输入样例:
6 11
3 4 70
1 2 1
5 4 50
2 6 50
5 6 60
1 3 70
4 6 60
3 6 80
5 1 100
2 4 60
5 2 80
输出样例:
4 70
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB
"""
def dijkstra(graph, start, end):
    """Dijkstra's algorithm for shortest paths
    graph is a dictionary of dictionaries, e.g.
    { 'a': {'b':1, 'c':2},
      'b': {'c':1},
      'c': {'a':1} }
    """
    Q = set(graph.keys())
    dist = dict.fromkeys(Q, float('inf'))
    prev = dict.fromkeys(Q, None)
    dist[start] = 0
    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        if dist[u] == float('inf') or u == end:
            break
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist[end], prev


def main():
    n, m = map(int, input().split())
    graph = {}
    for i in range(1, n + 1):
        graph[i] = {}
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    min_len = float('inf')
    min_node = 0
    for i in range(1, n + 1):
        max_len = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            max_len = max(max_len, dijkstra(graph, i, j)[0])
        if max_len < min_len:
            min_len = max_len
            min_node = i
    print(min_node, min_len)

if __name__ == '__main__':
    main()

