#include "bits/stdc++.h"

using namespace std;

vector<int> graph[102];
bool visited[102];
int n;
bool flag;
int calc_manhattan(pair<int,int> a , pair<int,int> b) {
    return abs(a.first-b.first)+ abs(a.second - b.second);
}

void bfs(int now) {
    queue<int> Q;
    Q.push(now);
    visited[now] = true;
    while (!Q.empty()) {
        int now = Q.front();
        if(now == n+1){
            flag = true;
        }
        Q.pop();
        for (int next: graph[now]) {
            if(!visited[next]) {
                visited[next] = true;
                Q.push({next});
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<pair<int ,int>> V;
        flag = false;
        for (int i = 0; i < n + 2; ++i) {
            int a , b;
            cin >> a >> b;
            V.push_back({a,b});
            visited[i] = false;
            graph[i].clear();
        }
        for (int i = 0; i < n + 2; ++i) {
            for (int j = i+1; j < n + 2; ++j) {
                if(calc_manhattan(V[i],V[j]) <= 1000) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }
        bfs(0);
        if (flag) {
            cout << "happy" << '\n';
        }else {
            cout << "sad" << '\n';
        }
    }
}#include "bits/stdc++.h"

using namespace std;

vector<int> graph[102];
bool visited[102];
int n;
bool flag;
int calc_manhattan(pair<int,int> a , pair<int,int> b) {
    return abs(a.first-b.first)+ abs(a.second - b.second);
}

void bfs(int now) {
    queue<int> Q;
    Q.push(now);
    visited[now] = true;
    while (!Q.empty()) {
        int now = Q.front();
        if(now == n+1){
            flag = true;
        }
        Q.pop();
        for (int next: graph[now]) {
            if(!visited[next]) {
                visited[next] = true;
                Q.push({next});
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<pair<int ,int>> V;
        flag = false;
        for (int i = 0; i < n + 2; ++i) {
            int a , b;
            cin >> a >> b;
            V.push_back({a,b});
            visited[i] = false;
            graph[i].clear();
        }
        for (int i = 0; i < n + 2; ++i) {
            for (int j = i+1; j < n + 2; ++j) {
                if(calc_manhattan(V[i],V[j]) <= 1000) {
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }
        bfs(0);
        if (flag) {
            cout << "happy" << '\n';
        }else {
            cout << "sad" << '\n';
        }
    }
}