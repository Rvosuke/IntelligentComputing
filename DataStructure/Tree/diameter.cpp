#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
int h[N], e[N], ne[N], idx;
int n;

void add(int a, int b)
{
    e[idx] = b;
    ne[idx] = h[a];
    h[a] = idx++;
}

pair<int, int> bfs(int x)
{
    vector<bool> st(N, false);
    queue<int> q;
    q.push(x)

        vector<int>
            dist(N, 0);
    int ld = 0;
    int ln = x;
    while (q.size())
    {
        int t = q.front();
        q.pop();
        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (!st[j])
            {
                st[j] = true;
                q.push(j);
                dist[j] = dist[t] + 1;
                if (dist[j] > ld)
                {
                    ld = dist[j];
                    ln = j;
                }
            }
        }
    }
    return {ln, ld};
}

int main()
{
    cin >> n;
    memset(h, -1, sizeof h);
    idx = 0;
    for (int i = 0; i < n - 1; i++)
    {
        int u, v;
        cin >> u >> v;
        add(u, v);
        add(v, u);
    }
    pair<int, int> n1 = bfs(1);
    pair<int, int> n2 = bfs(n1.first);
    cout << n2.second << endl;
    return 0;
}