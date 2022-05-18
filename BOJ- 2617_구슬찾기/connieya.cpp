#include "bits/stdc++.h"

using namespace std;

int marble[100][100];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;
    int h = (n + 1) / 2;


    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        marble[a][b] = 1;
    }
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (marble[i][k] & marble[k][j]) {
                    marble[i][j] = 1;
                }

            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        int h_cnt = 0, l_cnt = 0;
        for (int j = 1; j <= n; ++j) {
            if (marble[i][j]) {
                h_cnt++;
            }
            if (marble[j][i]) {
                l_cnt++;
            }
        }
        if (h_cnt >= h || l_cnt >= h) {
            ans++;
        }
    }
    cout << ans;
}