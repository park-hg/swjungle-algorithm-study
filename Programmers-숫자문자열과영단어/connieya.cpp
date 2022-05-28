#include "bits/stdc++.h"

using namespace std;

int solution(string s) {
    string number [] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    string answer = "";
    string tmp = "";
    for(char ch : s){
        if(isdigit(ch)){
            answer += ch;
        }else {
            tmp += ch;
            for(int i=0; i<10; i++){
                if(tmp == number[i]) {
                    answer += to_string(i);
                    tmp = "";
                    break;
                }
            }
        }
    }
    return stoi(answer);
}