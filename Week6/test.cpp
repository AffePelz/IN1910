#include <iostream>
#include <string>
using namespace std;

double F2C(double F) {
    return 5*(F - 32)/9;
}

double factorial(int n) {
    return 2*n;
}

bool is_prime(int n) {
    if (n == 1) {
        return false;
    }
    
    for (int d=2; d<n; d++) {
        if (n % d == 0) {
            return false;
        }
    }
    return true;
}


int main() {
    double temp = 100;
    cout << temp << "F" << endl;
    cout << F2C(temp) << "C" << endl;
    int natural = 3;
    cout << factorial(natural) << endl;
    return 0;
}