#include <bits/stdc++.h>

using namespace std;

bool cmp(int a, int b) {
    return a > b;
}

long long solution(int n, vector<int> works) {
    long long answer = 0;
    sort(works.begin(), works.end() , cmp);
    while(1){
        if(n == 0) break;
        int mx = works[0];
        for(auto &w : works){
            if(w == mx){
                w--;
                n--;
            }
            if(n == 0) break;
        }
    }
    for(auto w : works){
        if(w < 0) continue;
        answer += w*w;
    }
    return answer;
}