#include <bits/stdc++.h>

using namespace std;

vector<int> appeach;
vector<int> lions(11);
vector<int> ans(11);
int mx = 0;

void getScore(vector<int> lion) {
    int sum = 0;
    for(int i=0; i< 11; i++) {
        if(lions[i] > appeach[i]) {
            sum += 10-i;
        }
    }
    if(sum > mx) {
        cout << sum << '\n';
        mx = sum;
        ans = lions;
    }
}

void dfs(int L , int arrow , vector<int> &lion) {
    if(arrow < 0) return;
    if(L == 11) {
        getScore(lion);
        return;
    }

    for(int i=0; i<= appeach[L]+1; i++){
        lions[L] = arrow-i;
        dfs(L+1, arrow - arrow-i , lion);
    }

}

vector<int> solution(int n, vector<int> info) {
    appeach = info;
    vector<int> lion(11);
    vector<int> ret(12,-1);
    dfs(0,n,lion);
    for(auto l : ans) {
        cout << l << ' ';
    }
    cout << '\n';

    return ret;
}