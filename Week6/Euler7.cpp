#include <iostream>

using namespace std;

bool is_prime(int n) {
    if (n == 1) {
        return false;
    }
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return false;
    }
    }
    return true;
}

int sum_prime(int n) {
    int sum = 0;
    for (int i = 2; i < n; i++) {
        if (is_prime(i)) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    std::cout << sum_prime(200) << std::endl;
    return 0;
}