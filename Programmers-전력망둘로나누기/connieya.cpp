#include <bits/stdc++.h>

using namespace std;

vector<int> graph[101];
bool visited[101];

void dfs(int start ,int prev , int a, int b){
    visited[start] = true;
    for(int next : graph[start]) {
        if(next == prev) continue;
        if( (start == a && next == b) || (start == b && next == a ) ) continue;
        dfs(next , start , a, b);
    }
}

void init(int n){
    for(int i=1; i<=n; i++){
        visited[i] = false;
    }
}

int calc(int n){
    int cnt = 0;
    for(int i=1; i<=n; i++){
        cout << visited[i] << ' ';
        cnt += visited[i] ? 1 : -1;
    }
    cout << '\n';

    cnt = cnt < 0 ? -cnt : cnt;
    return cnt;
}

int solution(int n, vector<vector<int>> wires) {
    int answer = INT_MAX;
    for(int i=0; i< n-1; i++){
        graph[wires[i][0]].push_back(wires[i][1]);
        graph[wires[i][1]].push_back(wires[i][0]);
    }

    for(int i=0; i<n-1; i++){
        int a = wires[i][0];
        int b = wires[i][1];
        dfs(1,-1, a,b);
        int res = calc(n);
        answer = min(res,answer);
        init(n);

    }
    return answer;
}