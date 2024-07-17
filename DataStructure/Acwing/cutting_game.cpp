#include <bits/stdc++.h>
using namespace std;
using LL = long long;
const int INF = 0x3f3f3f3f;
const LL mod = 1e9 + 7;
const int N = 200005;

int a[N], b[N];

struct Node
{
    int x1, x2, y1, y2;
} d[N];
int main()
{
    int _;
    scanf("%d", &_);
    while (_--)
    {
        int h, w, n, m;
        scanf("%d%d%d%d", &h, &w, &n, &m);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d%d", &a[i], &b[i]);
        }
        int x1 = 1, x2 = h, y1 = 1, y2 = w;
        for (int i = 1; i <= m; i++)
        {
            char op;
            int k;
            scanf(" %c%d", &op, &k);
            if (op == 'U')
            {
                x1 += k;
            }
            else if (op == 'D')
            {
                x2 -= k;
            }
            else if (op == 'L')
            {
                y1 += k;
            }
            else
            {
                y2 -= k;
            }
            d[i] = {x1, x2, y1, y2};
        }
        int ans1 = 0, ans2 = 0;
        for (int i = 1; i <= n; i++)
        {
            int l = 1, r = m + 1;
            while (l < r)
            {
                int mid = l + r >> 1;
                auto [x1, x2, y1, y2] = d[mid];
                if (!(a[i] >= x1 && a[i] <= x2 && b[i] >= y1 && b[i] <= y2))
                    r = mid;
                else
                    l = mid + 1;
            }
            if (l != m + 1)
            {
                if (l % 2 == 1)
                    ans1++;
                else
                    ans2++;
            }
        }
        printf("%d %d\n", ans1, ans2);
    }
    return 0;
}
