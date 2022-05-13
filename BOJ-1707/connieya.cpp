#include "bits/stdc++.h"

#define INF 20001
#define BLACK -1

using namespace std;

int n, m;
vector<int> graph[INF];
int checked[INF];
bool visited[INF];

void init(){
    for (int i = 1; i <= n; ++i) {
        graph[i].clear();
        checked[i] = 0;
        visited[i] = false;
    }
}

void dfs(int start , int color){
    visited[start] = true;
    checked[start] = color;
    for (int next : graph[start]) {
        if(!visited[next]){
            dfs(next ,color*-1);
        }
    }
}

bool isBipartiteGraph(int start){
    int color = checked[start];
    for (int next : graph[start]) {
        if (checked[next] == color) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        string answer = "YES";
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        for (int i = 1; i <= n; ++i) {
            if(checked[i] == 0){
                dfs(i,BLACK);
            }
        }
        for(int i=1; i<=n; i++){
            if(!isBipartiteGraph(i)){
                answer = "NO";
                break;
            }
        }
        cout << answer << '\n';
        init();
    }
}