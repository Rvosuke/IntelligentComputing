#include <bits/stdc++.h>
using namespace std;

// these define are so interesting
#define flase false
#define int long long
#define itn int
#define enld endl
#define elnd endl
#define ednl endl
#define endl '\n'

bool cmp(int a, int b)
{
    return a > b;
}
bool cmp1(pair<int, int> a, pair<int, int> b)
{
    return a.first > b.first;
}
struct Compare
{
    bool operator()(int a, int b) const
    {
        return a > b;
    }
};

void solve()
{
    int n, k;
    cin >> n >> k;
    vector<int> m(n + 1), p(n + 1);  // we get n's position, why n+1? maybe start with 1
    for (int i = 1; i <= n; i++)
        cin >> m[i];
    for (int i = 1; i <= n; i++)
        cin >> p[i];
    vector<int> dp(n + 1, 0);
    dp[1] = p[1];
    for (int i = 2; i <= n; i++)
    {
        if (m[i] - m[i - 1] > k)
        {
            dp[i] = dp[i - 1] + p[i];
        }
        else
        {
            dp[i] = max(dp[i - 1], p[i]);  // here is the key point, but why?
            for (int j = i - 1; j >= 0; j--)
            {
                if (m[i] - m[j] > k)
                {
                    dp[i] = max(dp[i], dp[j] + p[i]);
                    break;
                }
            }
        }
    }
    cout << dp[n] << endl;
}
signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int _;
    cin >> _;
    while (_--)
        solve();
    return 0;
}