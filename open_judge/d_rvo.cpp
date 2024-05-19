#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n, k;
    cin >> n >> k;
    vector<int> m(n + 1), p(n + 1);
    for (int i = 1; i <= n; ++i)
    {
        cin >> m[i];
    }
    for (int i = 1; i <= n; ++i)
    {
        cin >> p[i];
    }
    vector<int> dp(n + 1, 0);
    for (int i = 2; i <= n; ++i)
    {
        if (m[i] - m[i - 1] > k)
        {
            dp[i] += p[i];
        }
        else
        {
            dp[i] = max(dp[i - 1], p[i]);
            for (int j = i - 1; j >= 1; j++)
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

int main()
{
    int _;
    cin >> _;
    while (_--)
    {
        solve();
    };
    return 0;
}