#include <iostream>
#include <bits/stdc++.h> 
#include <vector>
#include <cmath>
using namespace std;

double stirling(int x) {
    double func = x*log(x) - x;
    return func;
}

int main() {
    vector<int> values{2,5,10,50,100,1000};
    for (int p: values) {
        cout << "Approx x = " << p << ":   " << stirling(p) <<"\n";
    }
    cout << endl;
    for (int p: values) {
        cout << "Analytic x = " << p << ":   " << std::lgamma(p) <<"\n";
    }
    return 0;
}