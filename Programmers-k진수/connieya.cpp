#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

string a = "";


void translate(int n , int k){
    if(n == 0) return ;
    translate(n/k,k);
    a += to_string(n%k);
}

bool isPrime(ll num){
    if(num <= 1) return false;
    if(num == 2) return true;
    for(ll i=2; i*i <= num; i++){
        if(num % i == 0) return false;
    }
    return true;
}

int solution(int n, int k) {
    int answer = 0;
    translate(n,k);
    for(auto &ch : a){
        if(ch == '0') ch = ' ';
    }
    stringstream iss(a);
    string str;
    while(iss >> str){
        string tmp = str;
        if(!tmp.size()) continue;
        answer += isPrime(stoll(tmp));
    }
    return answer;
}