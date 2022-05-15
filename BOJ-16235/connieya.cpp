#include "bits/stdc++.h"

using namespace std;

int energy[11][11];
int ground[11][11];
vector<int> tree[11][11];
int n, m, k;
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

void input() {
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            cin >> energy[i][j];
            ground[i][j] = 5;
        }
    }

    for (int i = 0; i < m; ++i) {
        int x, y, age;
        cin >> x >> y >> age;
        tree[x][y].push_back(age);
    }
}

void spring_summer(int x, int y) {
    vector<int> tmp;
    sort(tree[x][y].begin(), tree[x][y].end());
    int add = 0;
    for (auto &t: tree[x][y]) {
        if (t <= ground[x][y]) {
            ground[x][y] -= t;
            tmp.push_back(t + 1);
        } else {
            add += t / 2;
        }
    }
    tree[x][y].clear();
    tree[x][y] = tmp;
    ground[x][y] += add;
}

void breed(int x, int y) {
    for (int i = 0; i < 8; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 1 || nx > n || ny < 1 || ny > n) continue;
        tree[nx][ny].push_back(1);
    }
}

void fall_winter(int x, int y) {
    for (auto &t: tree[x][y]) {
        if (t % 5 == 0) {
            breed(x, y);
        }
    }
}

void solve() {
    while (k--) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (tree[i][j].size() > 0) {
                    spring_summer(i, j);
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (tree[i][j].size() > 0) {
                    fall_winter(i, j);
                }
                ground[i][j] += energy[i][j];
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            ans += tree[i][j].size();
        }
    }

    cout << ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m >> k;
    input();
    solve();
}