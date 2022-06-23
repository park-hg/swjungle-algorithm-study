#include <bits/stdc++.h>

using namespace std;

int dir[3][201];
vector<pair<int,int>> graph[201];

void dijkstra(int idx , int start , int n) {
    priority_queue<pair<int,int>> pq;
    pq.push({0,start});
    for(int i=1; i<=n; i++) {
        dir[idx][i] = INT_MAX;
    }
    dir[idx][start] = 0;

    while(!pq.empty()) {
        auto cur = pq.top();
        int now = cur.second;
        int cost = -cur.first;
        pq.pop();
        if(dir[idx][now] < cost) continue;

        for(auto nxt : graph[now]) {
            int next_cost = nxt.second;
            int next = nxt.first;
            if(dir[idx][next] > next_cost + cost) {
                dir[idx][next] = next_cost + cost;
                pq.push({-(next_cost+cost), next});
            }
        }
    }
}


int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = 1e7;
    for(auto fare : fares){
        graph[fare[0]].push_back({fare[1],fare[2]});
        graph[fare[1]].push_back({fare[0],fare[2]});
    }
    dijkstra(0,s,n);
    dijkstra(1,a,n);
    dijkstra(2,b,n);

    for(int i=1; i<=n; i++){
        answer = min(answer , dir[0][i] + dir[1][i] + dir[2][i]);
    }

    return answer;
}