#include <bits/stdc++.h>

using namespace std;

int time_to_min(string str) {
    int h = (str[0]-'0')*10 + (str[1]-'0');
    int m = (str[3]-'0')*10 + (str[4]-'0');
    return h*60 + m;
}

string min_to_time(int t){
    string h = to_string(t / 60);
    if(h.size() == 1) h = '0'+h;
    string m = to_string(t % 60);
    if(m.size() == 1) m = '0'+m;
    return h+":"+m;

}

string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "";
    vector<int> t_list;
    for(auto t : timetable){
        t_list.push_back(time_to_min(t));
    }
    sort(t_list.begin() , t_list.end() );
    int init = 540; // 09:00 시간을 분으로 환산
    int idx = 0;
    int cnt;
    while(n--) {
        cnt = 0;
        while(idx < t_list.size() && t_list[idx] <= init && cnt < m){
            idx++;
            cnt++;
        }
        init += t;
    }
    if(cnt < m) return min_to_time(init-t);
    return min_to_time(t_list[idx-1] -1);
}