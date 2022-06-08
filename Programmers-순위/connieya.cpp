#include <bits/stdc++.h>

using namespace std;

bool arr[101][101];

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    for(auto &result : results){
        arr[result[0]][result[1]] = true;
    }

    for(int k=1; k<=n; k++) {
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(arr[i][k] && arr[k][j]) arr[i][j] = true;
            }
        }
    }

    for(int i=1; i<=n; i++){
        int cnt = 0;
        for(int j=1; j<=n; j++){
            if(arr[i][j] || arr[j][i]) cnt++;
        }
        answer += (cnt == n-1);
    }

    return answer;
}