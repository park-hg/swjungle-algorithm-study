#include <bits/stdc++.h>

using namespace std;

set<int> s;
string nums;
bool visited[8];

bool isPrime(int num) {
    if(num <= 1 ) return false;
    if(num == 2) return true;
    for(int i=2; i * i <= num; i++) {
        if(num % i == 0) return false;
    }
    return true;
}


int solution(string numbers) {
    sort(numbers.begin() , numbers.end());
    do {
        string tmp = "";
        for(char ch : numbers) {
            tmp += ch;
            if(isPrime(stoi(tmp))) s.insert(stoi(tmp));
        }
    }while(next_permutation(numbers.begin() , numbers.end() ) );

    return s.size();
}