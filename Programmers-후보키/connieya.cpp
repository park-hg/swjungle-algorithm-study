#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> v_comp;

void dfs(int L , int n , int start) {

    for(int i=start; i<n; i++){
        if(!visited[i]){
            visited[i] = true;
            v_comp.push_back(i);
            dfs(L+1,n, i+1);
            v_comp.pop_back();
        }
    }
}

int solution(vector<vector<string>> relation) {
    int answer = 0;
    int len = relation.size();
    for(int i=0; i<len; i++){
        for(auto r : relation[i]){
            cout << r << ' ';
        }
        cout << '\n';
    }
    return answer;
}