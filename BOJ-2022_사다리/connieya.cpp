#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    double x,y,c;
    cin >> x >> y >> c;
    double lt = 0 , rt = min(x,y);
    while (rt -lt > 1e-6){
        double mid = (lt+rt)/2;
        double l = sqrt(x*x - mid*mid);
        double r = sqrt(y*y - mid*mid);
        double m = l*r / (l+r);
        if (m > c) {
            lt = mid;
        }else {
            rt = mid;
        }
    }
    cout << fixed << setprecision(3) << rt;
}