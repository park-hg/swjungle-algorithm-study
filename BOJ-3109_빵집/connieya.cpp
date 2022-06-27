#include "bits/stdc++.h"

using namespace std;

int r, c;
char board[10001][501];

int dx[] = {-1, 0, 1};
int dy[] = {1, 1, 1};

bool dfs(int x, int y) {
    if (y == c - 1) {
        return true;
    }
    for (int i = 0; i < 3; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || ny < 0 || nx >= r || board[nx][ny] == 'x') continue;
        if (board[nx][ny] == '.') {
            board[nx][ny] = 'o';
            if (dfs(nx, ny)) return true;
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> r >> c;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < r; i++) {
        dfs(i, 0);
    }

//    for (int i = 0; i < r; ++i) {
//        for (int j = 0; j < c; ++j) {
//            cout << board[i][j] << ' ';
//        }
//        cout << '\n';
//    }

    int ans = 0;
    for (int i = 0; i < r; i++) {
        ans += board[i][c - 1] == 'o';
    }
    cout << ans;
}