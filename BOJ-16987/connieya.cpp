#include "bits/stdc++.h"

using namespace std;

int n;
int ans;
vector<pair<int,int>> v; // 내구도 , 무게
void solve(int cur) {
    if(cur == n) {
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            cnt += v[i].first <= 0;
        }
        if(cnt > ans){
            ans = cnt;
        }
        return;
    }

    if(v[cur].first <= 0) {
        solve(cur+1);

    }else{
        bool flag = true;
        for (int i = 0; i < n; ++i) {
            if(i == cur || v[i].first <= 0) continue;
            v[cur].first -= v[i].second;
            v[i].first -= v[cur].second;
            flag = false;
            solve(cur + 1);
            v[cur].first += v[i].second;
            v[i].first += v[cur].second;
        }
        if(flag) solve(n);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int d,w;
        cin >> d >> w;
        v.push_back({d,w});
    }
    solve(0);
    cout << ans;
}