#include "bits/stdc++.h"

using namespace std;

string str;
int max_num;
vector<int> ans;
bool check[51];

void dfs(int L , int len) {
    if(L == len){
        for(auto a : ans){
            cout << a << ' ';
        }
        exit(0);
    }
    if(L+1 <len){
        int num = (str[L]-'0')*10 + str[L+1]-'0';
        if(num <=max_num && !check[num]){
            check[num] = true;
            ans.push_back(num);
            dfs(L+2,len);
            check[num] = false;
            ans.pop_back();
        }
    }
    int num = str[L]-'0';
    if(num && !check[num]){
        check[num] = true;
        ans.push_back(num);
        dfs(L+1,len);
        check[num] = false;
        ans.pop_back();
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> str;
    int len = str.length();
    if(len <=9){
        for (char ch: str) {
            cout << ch << ' ';
        }
        exit(0);
    }
    max_num = (len-9)/2 + 9;
    dfs(0,len);
}