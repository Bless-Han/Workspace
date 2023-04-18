/*
7-9 旅游规划
分数 25
作者 陈越
单位 浙江大学
有了一张自驾旅游路线图，你会知道城市间的高速公路长度、以及该公路要收取的过路费。现在需要你写一个程序，帮助前来咨询的游客找一条出发地和目的地之间的最短路径。如果有若干条路径都是最短的，那么需要输出最便宜的一条路径。

输入格式:
输入说明：输入数据的第1行给出4个正整数N、M、S、D，其中N（2≤N≤500）是城市的个数，顺便假设城市的编号为0~(N−1)；M是高速公路的条数；S是出发地的城市编号；D是目的地的城市编号。随后的M行中，每行给出一条高速公路的信息，分别是：城市1、城市2、高速公路长度、收费额，中间用空格分开，数字均为整数且不超过500。输入保证解的存在。

输出格式:
在一行里输出路径的长度和收费总额，数字间以空格分隔，输出结尾不能有多余空格。

输入样例:
4 5 0 3
0 1 1 20
1 3 2 30
0 3 4 10
0 2 2 20
2 3 1 20
输出样例:
3 40
代码长度限制
16 KB
Java (javac)
时间限制
800 ms
内存限制
64 MB
其他编译器
时间限制
400 ms
内存限制
64 MB
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int INF = 0x3f3f3f3f;
int main()
{
    int n, m, s, d;
    cin >> n >> m >> s >> d;
    vector<vector<int> > dis(n, vector<int>(n, INF));
    vector<vector<int> > cost(n, vector<int>(n, INF));
    for (int i = 0; i < m; i++)
    {
        int c1, c2, d, c;
        cin >> c1 >> c2 >> d >> c;
        dis[c1][c2] = dis[c2][c1] = d;
        cost[c1][c2] = cost[c2][c1] = c;
    }
    vector<int> dis_min(n, INF);
    vector<int> cost_min(n, INF);
    vector<bool> visited(n, false);
    dis_min[s] = 0;
    cost_min[s] = 0;
    for (int i = 0; i < n; i++)
    {
        int u = -1, min = INF;
        for (int j = 0; j < n; j++)
        {
            if (visited[j] == false && dis_min[j] < min)
            {
                u = j;
                min = dis_min[j];
            }
        }
        if (u == -1)
            break;
        visited[u] = true;
        for (int v = 0; v < n; v++)
        {
            if (visited[v] == false && dis[u][v] != INF)
            {
                if (dis_min[u] + dis[u][v] < dis_min[v])
                {
                    dis_min[v] = dis_min[u] + dis[u][v];
                    cost_min[v] = cost_min[u] + cost[u][v];
                }
                else if (dis_min[u] + dis[u][v] == dis_min[v])
                {
                    if (cost_min[u] + cost[u][v] < cost_min[v])
                    {
                        cost_min[v] = cost_min[u] + cost[u][v];
                    }
                }
            }
        }
    }
    cout << dis_min[d] << " " << cost_min[d];
    return 0;
}

// Language: cpp