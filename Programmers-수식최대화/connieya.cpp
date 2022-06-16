#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<ll> numbers;
vector<char> op;

void init(string ex){
    ll res = 0;
    for(auto e : ex){
        if(isdigit(e)){
            res = res * 10 + (e-'0');
        }else {
            numbers.push_back(res);
            res = 0;
            op.push_back(e);
        }
    }
    numbers.push_back(res);
}

ll calc(ll a , ll b , char op){
    if(op == '+') return a+b;
    if(op == '*') return a*b;
    return a-b;
}

long long solution(string expression) {
    long long answer = 0;
    init(expression);
    char arr[] = {'*','-','+'};
    sort(arr,arr+3);

    do {
        vector<ll> num = numbers;
        vector<char> o = op;
        for(int i=0; i<3; i++){
            for(int k=0; k < o.size(); k++){
                if(o[k] == arr[i]) {
                    ll result = calc(num[k],num[k+1],arr[i]);
                    num[k] = result;
                    num.erase(num.begin()+k+1);
                    o.erase(o.begin()+k);
                    k--;
                }
            }
        }
        ll tmp = abs(num[0]);
        if(tmp > answer) answer = tmp;

    }while(next_permutation(arr,arr+3));


    return answer;
}