#include <bits/stdc++.h>

using namespace std;

int calcTime(string str) {
    int hour = (str[0] - '0') * 10 + (str[1] - '0');
    int minute = (str[3] - '0') * 10 + (str[4] - '0');
    return hour * 60 + minute;
}

vector<int> solution(vector<int> fees, vector <string> records) {
    vector<int> vehicle[10000]; // 차량 번호는 4자리이다. 
    vector<int> answer;
    for (string record: records) {
        stringstream iss(record);
        string a, b, c;
        iss >> a >> b >> c;
        vehicle[stoi(b)].push_back(calcTime(a));
    }
    for (int i = 0; i < 10000; i++) {
        if (vehicle[i].empty()) continue;
        if (vehicle[i].size() & 1) vehicle[i].push_back(23 * 60 + 59);
        int sum = 0;
        for (int j = 1; j < vehicle[i].size(); j += 2) {
            sum += vehicle[i][j] - vehicle[i][j - 1];
        }
        int cost = fees[1];
        if (sum > fees[0]) {
            cost += (sum - fees[0] + fees[2] - 1) / fees[2] * fees[3];
        }

        answer.push_back(cost);

    }

    return answer;
}