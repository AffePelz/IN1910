#include <iostream>
#include <map>

using namespace std;

class Polynomial {
private:
    map<int, int> a;
public:
    Polynomial Polynomial(a) {
        
    }
};

int main() {
    map<int, int> partners;
    map<string, double> params;
    map<int, string> students;

    partners[2] = 4;
    params["friction"] = 0.4;
    students[147] = "John Doe";

    for (pair<string, double> element: params) {
        cout << element.first;
        cout << " -> ";
        cout << element.second;
        cout << endl;
}
}