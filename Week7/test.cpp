#include <iostream>
using namespace std;

int main () {
    int n = 100;
    double x[n];
    for (int i=0; i < n; i++) {
        x[i] = 0;
        // cout << x[i] << endl;
    }
    int primes[] = {2, 3, 5, 7, 11};
    int size = sizeof(primes) / sizeof(primes[0]);
    // cout << sizeof(primes[0]) << endl;
    int a = 10;
    int *b = &a;
    cout << b << endl;
    return 0;
}