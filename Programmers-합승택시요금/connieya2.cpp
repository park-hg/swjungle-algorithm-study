#include <bits/stdc++.h>

using namespace std;

int dir[201][201];

void init(int n){
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            if(i == j) {
                continue;
            }
            dir[i][j] = 1e7;
        }
    }
}

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 1e7;
    init(n);
    for(auto fare : fares){
        dir[fare[0]][fare[1]] = fare[2];
        dir[fare[1]][fare[0]] = fare[2];
    }

    for(int k=1; k<=n; k++) {
        for(int i=1; i<=n; i++) {
            for(int j=1; j<=n; j++){
                if(dir[i][j]  > dir[i][k]+dir[k][j]){
                    dir[i][j] = dir[i][k] +dir[k][j];
                }
            }
        }
    }

    for(int i=1; i<=n; i++){
        // cout << dir[i][s] << '\n';
        answer = min(answer , dir[i][s] + dir[i][a] + dir[i][b]);
    }

    return answer;
}