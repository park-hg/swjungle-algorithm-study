#include <bits/stdc++.h>

using namespace std;

unordered_map<string , int> mp;
vector<int> List[4][3][3][3];

vector<int> solution(vector<string> infos, vector<string> query) {
    mp["-"] =  0;
    mp["cpp"] = 1;
    mp["java"] = 2;
    mp["python"] = 3;
    mp["backend"] = 1;
    mp["frontend"] = 2;
    mp["junior"] = 1;
    mp["senior"] = 2;
    mp["chicken"] = 1;
    mp["pizza"] = 2;

    for(auto info : infos) {
        stringstream iss(info);
        string a,b,c,d;
        int score;
        iss >> a >> b >> c >> d >> score;
        int arr[4] = {mp[a] , mp[b] , mp[c] , mp[d]};
        for(int i=0; i< (1<<4); i++) {
            int idx[4] = {0};
            for(int j=0; j<4; j++) {
                if(i & (1 << j)) {
                    idx[j] = arr[j];
                }
            }
            List[idx[0]][idx[1]][idx[2]][idx[3]].push_back(score);
        }
    }

    for(int i=0; i < 4; i++) {
        for(int j=0; j<3; j++){
            for(int k=0; k<3; k++){
                for(int l=0; l<3; l++){
                    sort(List[i][j][k][l].begin() , List[i][j][k][l].end());
                }
            }
        }
    }

    vector<int> answer;
    for(auto str : query) {
        stringstream iss(str);
        string a ,b ,c ,d ,temp;
        int score;
        iss >> a >> temp >> b >> temp >> c >> temp >> d >> score;
        auto & sList = List[mp[a]][mp[b]][mp[c]][mp[d]];

        vector<int>::iterator low = lower_bound(sList.begin() , sList.end() , score);
        answer.push_back(sList.end() - low);
    }
    return answer;
}