#include <bits/stdc++.h>
using namespace std;
list<int> l;
list<int> ::iterator its[10000015];
list<int> ::iterator cursor;
stack<pair<int,int>> erased;

string solution(int n, int k, vector<string> cmd) {
    for(int i=0; i<= n; i++){
        l.push_back(i);
    }
    auto it = l.begin();
    for(int i= 0; i <=n; i++){
        its[i] = it;
        it++;
    }

    cursor = its[k];
    for(auto c : cmd) {
        if(c[0] == 'D') {
            int num = stoi(c.substr(2,100));
            while(num--){
                cursor++;
            }
        }else if(c[0] == 'C') {
            erased.push({*cursor , *(next(cursor))});
            cursor = l.erase(cursor);
            if(*cursor == n ) cursor--;
        }else if(c[0] == 'U') {
            int num = stoi(c.substr(2,100));
            while(num--){
                cursor--;
            }
        }else {
            int cur , nxt;
            tie(cur,nxt) = erased.top();
            erased.pop();
            its[cur] = l.insert(its[nxt] , cur);
        }
    }
    string answer(n,'X');
    for(auto x : l ){
        if(x != n) answer[x] = 'O';
    }
    return answer;
}