#include "bits/stdc++.h"

using namespace std;

int n, m;
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
vector<pair<int, int>> coin;
char board[21][21];
int ans = INT_MAX;

bool OOP(pair<int,int> &p) {
    return p.first < 0 || p.first >= n || p.second < 0 || p.second >= m;
}

void dfs(pair<int, int> a, pair<int, int> b, int cnt) {
    if(ans < cnt) return;
    if (cnt > 10) {
        return;
    }
    if (OOP(a) && OOP(b)) return;
    if (OOP(a) && !OOP(b)) {
        ans = min(ans, cnt);
        return;
    }
    if (!OOP(a) && OOP(b)) {
        ans = min(ans, cnt);
        return;
    }
    for (int i = 0; i < 4; ++i) {
        pair<int,int> an = {a.first+dx[i], a.second+dy[i]};
        pair<int,int> bn = {b.first+dx[i],b.second+dy[i]};
        if(board[an.first][an.second] == '#'){
            an = a;
        }
        if(board[bn.first][bn.second] == '#'){
            bn = b;
        }
        dfs(an, bn, cnt + 1);

    }
}

void input() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> board[i][j];
            if (board[i][j] == 'o') {
                coin.push_back({i, j});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    input();
    dfs(coin[0], coin[1], 0);
    ans == INT_MAX ? cout << "-1" : cout << ans;
}