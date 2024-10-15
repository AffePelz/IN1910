#include <iostream>
using namespace std;

void reduction_by_halves(int n) {
    while (n > 0) {
        cout << n << "\n";
        n/=2;
    }
}

int main() {
    int  n = 1000;
    reduction_by_halves(n);
    return 0;
}