#include "bits/stdc++.h"

using namespace std;

vector<string> words;
string ans;

void bfs(string first) {
    queue<pair<string, int>> Q;
    Q.push({first, 0});
    while (!Q.empty()) {
        string target = Q.front().first;
        int start = Q.front().second;
        ans = target;
        Q.pop();
        for (int i = start; i < words.size(); i++) {
            if (words[i].length() == target.length() + 1)
                if (words[i].find(target) != string::npos) {
                    Q.push({words[i], i});
                    continue;
                }
            int idx = 0;
            int t_idx = 0;
            while (idx < words[i].length()) {
                if (words[i][idx] == target[t_idx]) {
                    t_idx++;
                }
                idx++;
            }
            if (t_idx == target.length()) {
                Q.push({words[i], i});
            }
        }

    }
}


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    string str, input;
    cin >> n >> str;
    while (n--) {
        cin >> input;
        words.push_back(input);
    }
    sort(words.begin(), words.end());
    bfs(str);
    cout << ans;
}