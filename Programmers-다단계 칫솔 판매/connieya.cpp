#include <bits/stdc++.h>

using namespace std;
unordered_map<string,int> total;
unordered_map<string,string> connect;


void calc(string name , int amount)
{
    if(name == "-") return;
    int profit = amount/10;
    total[name] += amount - profit;
    if(profit == 0) return;
    calc(connect[name] , profit);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    int len = enroll.size();
    for(int i=0; i<len; i++) {
        connect[enroll[i]] = referral[i];
    }
    for(int i=0; i<seller.size(); i++) {
        calc(seller[i], amount[i]*100);
    }
    vector<int> answer;
    for(string e : enroll){
        answer.push_back(total[e]);
    }
    return answer;
}