#include <bits/stdc++.h>

using namespace std;

struct Info {
    string original;
    string head;
    int number;

    Info(string o , string h ,int n ){
        original = o;
        head = h;
        number = n;
    }

    bool operator<(const Info &t)const{
        if(head.compare(t.head) == 0) {
            return number < t.number;
        }
        return head.compare(t.head) < 0;

    }
};

vector<string> solution(vector<string> files) {
    vector<string> answer;
    vector<Info> info;
    for(auto file : files){
        string tmp;
        int i;
        for(i=0; i<file.size(); i++){
            if(isdigit(file[i])){
                break;
            }else {
                tmp += toupper(file[i]);
            }
        }
        int res = 0;
        for(; i<file.size(); i++){
            if(isdigit(file[i])){
                res = res *10 + (file[i]-'0');
            }else {
                break;
            }
        }

        info.push_back(Info(file,tmp,res));
    }
    stable_sort(info.begin(), info.end());
    for(auto i : info){
        answer.push_back(i.original);
        cout << i.original << ' ' << i.head << ' ' << i.number << '\n';
    }
    return answer;
}