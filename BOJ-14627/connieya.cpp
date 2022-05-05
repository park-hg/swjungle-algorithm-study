#include "bits/stdc++.h"

#define MX 1000000

typedef long long ll;
using namespace std;

ll arr[MX + 1];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll s, c;
    cin >> s >> c;
    ll lt = 1, rt = 0, sum = 0 , ans;
    for (int i = 0; i < s; ++i) {
        cin >> arr[i];
        sum += arr[i];
        if(arr[i] > rt){
            rt= arr[i];
        }
    }
    while (lt <= rt) {
        ll mid = (lt + rt) / 2;
        ll cnt = 0;
        for (int i = 0; i < s; ++i) {
            cnt += arr[i] / mid;
        }
        if (cnt >= c) {
            lt = mid+1;
            ans = mid;
        } else {
            rt = mid-1;
        }
    }
    cout << sum - ans * c;
}