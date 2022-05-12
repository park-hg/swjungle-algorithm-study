#include <bits/stdc++.h>
using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    unordered_map<string , int> report_count;
    unordered_map<string , set<string> > report_list;
    unordered_map<string , set<string> > mp;

    for(auto &re : report) {
        stringstream iss(re);
        string a ,b;
        iss >> a >> b;
        report_list[a].insert(b);
        auto s = mp[b];
        if(s.find(a) == s.end()){
            report_count[b]++;
        }
        mp[b].insert(a);
    }

    for(auto &id : id_list) {
        auto list = report_list[id];
        int count = 0;
        for(auto l : list){
            if(report_count[l] >= k) count++;
        }
        answer.push_back(count);
    }
    return answer;
}