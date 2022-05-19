#include "bits/stdc++.h"

#define INF 1001

using namespace std;

vector<int> graph[INF];
vector<int> result;
int indegree[INF];

void solve(int n) {
    queue<int> Q;
    for (int i = 1; i <= n; ++i) {
        if (!indegree[i]) Q.push(i);
    }
    while (!Q.empty()) {
        int now = Q.front();
        Q.pop();
        result.push_back(now);
        for (int next: graph[now]) {
            indegree[next]--;
            if (!indegree[next]) Q.push(next);
        }
    }
}

void print(int n) {
    if (result.size() != n) {
        cout << 0;
        return;
    }

    for (int res: result) {
        cout << res << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m, cnt, prev, num;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        cin >> cnt;
        cin >> prev;
        for (int j = 1; j < cnt; ++j) {
            cin >> num;
            indegree[num]++;
            graph[prev].push_back(num);
            prev = num;
        }
    }
    solve(n);
    print(n);
}