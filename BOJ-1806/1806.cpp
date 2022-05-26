#include "bits/stdc++.h"

using namespace std;

int arr[100001];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, s;
    cin >> n >> s;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        sum += arr[i];
    }
    if (sum < s) {
        cout << 0;
        exit(0);
    }
    sum = arr[0];
    int lt = 0;
    int rt = 0;
    int ans = INT_MAX;
    while (rt < n) {
        if (sum < s) {
            rt++;
            sum += arr[rt];
        } else {
            if (ans > rt - lt+1) {
                ans = rt - lt+1;
            }
            sum -= arr[lt++];
        }
    }
    if(sum >= s && ans > rt-lt){
        ans = rt-lt;
    }
    cout << ans;
}