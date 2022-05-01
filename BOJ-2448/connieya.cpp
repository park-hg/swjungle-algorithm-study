#include "bits/stdc++.h"

using namespace std;

int n;


void func(int x, int y, int size , vector<string> &board) {
    if (size == 3) {
        board[x][y + 2] = '*';
        board[x + 1][y + 1] = board[x + 1][y + 3] = '*';
        board[x + 2][y] = board[x + 2][y + 1] = board[x + 2][y + 2] = board[x + 2][y + 3] = board[x + 2][y + 4] = '*';
        return;
    }
    func(x, y + size / 2, size / 2 , board);
    func(x + size / 2, y, size / 2 , board) ;
    func(x + size / 2, y + size, size / 2 , board);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    vector<string> board(n, string(n << 1, ' '));
    func(0, 0, n ,board);
    for (const auto& i : board) cout << i << '\n';

}