#include "bits/stdc++.h"

using namespace std;

int room[51][51];
bool checked[51][51];
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
int r, c, x, y, dir;

void rotate(){
    dir = (dir+3)%4;
}

int solve(){
    int cnt = 1;
    checked[x][y] = 1;
    while (1) {
        int i;
        bool flag = true;
        for(i=0; i<4; i++){
            rotate();
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if(room[nx][ny] == 0 && !checked[nx][ny]) {
                flag = false;
                checked[nx][ny] = 1;
                cnt++;
                x = nx;
                y = ny;
                break;
            }
        }
        if(flag) {
            if(room[x-dx[dir]][y-dy[dir]] == 1) break;
            x = x-dx[dir];
            y = y-dy[dir];
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> r >> c;
    cin >> x >> y >> dir;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cin >> room[i][j];
        }
    }
    cout << solve();
}