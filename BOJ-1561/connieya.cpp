#include "bits/stdc++.h"

using namespace std;
typedef long long ll;

ll arr[10001];
ll n, m, lt, rt, mx = 0;

ll check(ll mid){
    ll cnt = 0;
    for (int i = 0; i < m; ++i) {
        cnt += mid/arr[i]+1;
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    if (n <= m) {
        cout << n;
        exit(0);
    }
    for (int i = 0; i < m; ++i) {
        cin >> arr[i];
        if (arr[i] > mx) {
            mx = arr[i];
        }
    }
    lt = 0, rt = mx*n;
    while (lt +1 < rt) {
        ll mid = (lt + rt) / 2;
        if (check(mid) < n){
            lt = mid;
        }else {
            rt = mid;
        }
    }
    ll cnt = check(lt);
    for (int i = 0; i < m; ++i) {
        if (rt % arr[i] == 0){
            cnt++;
        }
        if (cnt == n){
            cout << i+1;
            exit(0);
        }
    }
}