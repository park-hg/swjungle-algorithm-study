#include <bits/stdc++.h>

using namespace std;

int INF = 1e6;
int par[17];
int visited[1<<17];
vector<int> graph[17];

void dfs(int prev , int cur) {
    par[cur] = prev;
    for(int next : graph[cur]){
        if(next == prev) continue;
        dfs(cur, next);
    }

}

int solve(vector<int> info , int state , int n){
    int &res = visited[state];
    int cnt = 0;
    if(res != -1) return res;
    res = 0;
    for(int i=0; i<n; i++){
        if(state & 1<<i){
            if(info[i]) cnt++;
            else res++;
        }
    }
    if(res <= cnt) return -INF;
    for(int i=1; i< n; i++) {
        if(state & 1 << i || ~state & 1 << par[i]) continue;
        res = max(res , solve(info , state | 1<< i , n));
    }
    return res;
}

int solution(vector<int> info, vector<vector<int>> edges) {
    int n = info.size();
    for(const auto &i : edges){
        graph[i[0]].push_back(i[1]);
        graph[i[1]].push_back(i[0]);
    }
    dfs(-1,0);
    fill(visited,visited+(1<<n) , -1);


    return solve(info , 1 , n);
}