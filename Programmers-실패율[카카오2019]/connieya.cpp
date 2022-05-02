#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<int> number(N+1);
    vector<pair<double,int>> v;
    int len = stages.size();
    for(int s : stages){
        number[s]++;
    }
    int p = 0;
    for(int i=1; i<=N; i++){
        double d = len - p;
        if(d == 0){
            v.push_back({0 , i});
        }else {
            v.push_back({number[i]/d , i});
        }
        p += number[i];
    }
    sort(v.begin(), v.end() ,[&](pair<double,int> &a , pair<double,int> &b){
        return a.first == b.first ? a.second < b.second : a.first > b.first;
    });

    for(auto p : v){
        answer.push_back(p.second);
    }
    return answer;
}