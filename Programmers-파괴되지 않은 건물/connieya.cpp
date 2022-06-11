#include <bits/stdc++.h>

using namespace std;

int dp[1002][1002];

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    int r = board.size();
    int c = board[0].size();
    for(auto s : skill){
        int type = s[0];
        int r1 = s[1] , c1 = s[2] , r2 =s[3] , c2 = s[4] , degree = s[5];
        if(type == 1){
            degree = -degree;
        }
        dp[r1][c1] += degree;
        dp[r1][c2+1] -= degree;
        dp[r2+1][c1] -= degree;
        dp[r2+1][c2+1] += degree;
    }
    for(int i=1; i<r; i++){
        for(int j=0; j<c; j++){
            dp[i][j] += dp[i-1][j];
        }
    }
    for(int i=1; i<c; i++){
        for(int j=0; j<r; j++){
            dp[j][i] += dp[j][i-1];
        }
    }
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            board[i][j] += dp[i][j];
            answer += board[i][j] > 0;
        }
    }
    return answer;
}