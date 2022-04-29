#include "bits/stdc++.h"

using namespace std;

vector<string> words;
unordered_map<string,int> mp;
string ans;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    string str, input;
    cin >> n >> str;
    mp[str]++;
    ans = str;
    while (n--) {
        cin >> input;
        words.push_back(input);
    }
    sort(words.begin(),words.end() ,[&](string a , string b){
        return a.length() < b.length();
    });
    for (auto word : words) {
        int len  = word.length();
        for (int i = 0; i < len; ++i) {
            string tmp = "";
            tmp = word.substr(0,i)+word.substr(i+1);
            if (mp[tmp]){
                mp[word]++;
                if (word.length() > ans.length()){
                    ans = word;
                }
            }
        }
    }
    cout << ans;
}