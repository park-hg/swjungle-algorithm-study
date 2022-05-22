#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int s_time , j_time , n , t, cnt;
    char color;
    cin >> s_time >> j_time >> n;
    int max_s = 0 , max_j = 0;
    priority_queue<pair<int, char>> pq;
    for (int i = 0; i < n; ++i) {
        cin >> t >> color >> cnt;
        if(color == 'B') {
            if(t > max_s) {
                int temp = t;
                while (cnt--) {
                    pq.push({temp ,color});
                    temp += s_time;
                }
                max_s = temp;
            }else { // max_s > t
                while (cnt--){
                    pq.push({max_s , color});
                    max_s += s_time;
                }
            }
        }else {

        }
    }

}