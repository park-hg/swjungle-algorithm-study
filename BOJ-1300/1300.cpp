#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n,k,ans;
    cin >> n >> k;
    int lt = 1, rt = k;
    while (lt <= rt) {
        int mid = (lt+rt)/2;
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            cnt += min(mid/i , n);
        }
        if (cnt >= k) {
            rt = mid-1;
            ans = mid;
        } else {
            lt = mid+1;
        }
    }
    cout << ans;
}