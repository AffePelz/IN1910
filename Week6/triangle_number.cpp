#include <iostream>
using namespace std;

double triangle(int n) {
    int s = 0;
    int i = 0;
    while (i < n+1) {
        s += i;
        i++;
    }
    return s;
}

void test_triangle() {
    std::vector<int> expected {0, 1, 3, 6, 10, 15};

    for (int i = 0; i < expected.size(); i++) {
        std::cout << triangle(i) << ", " << expected[i] << std::endl;
        assert(triangle(i) == expected[i]);
    }

    int triangle_76 = 76*(76+1) / 2;
    assert(triangle(76) == triangle_76);
}

int main() {
    for (int i=1; i<6; i++) {
        cout << triangle(i) << endl;
    }
    int k = 761;
    cout << "n = " << k << ":  "<< triangle(k) << endl;
    int s = (k*(k+1))/2;
    cout << "Analytic for n = " << k << ":   " << s << endl;

    int n;

    cout << "Please enter a number: ";
    cin >> n;
    cout << triangle(n) << endl;
    return 0;
}