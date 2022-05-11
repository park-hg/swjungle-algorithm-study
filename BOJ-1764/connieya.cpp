#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    unordered_map<string ,int > mp;
    int n,m ;
    string name;
    cin >> n >> m;
    for (int i = 0; i < n+m; ++i) {
        cin >> name;
        mp[name]++;
    }
    vector<string> ans;
    for(auto &m : mp){
        if(m.second > 1){
            ans.push_back(m.first);
        }
    }
    sort(ans.begin(),ans.end());
    cout << ans.size() << '\n';
    for(auto s : ans){
        cout << s << '\n';
    }
}