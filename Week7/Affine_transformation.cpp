#include <iostream>

using namespace std;

struct Point {
        double x;
        double y;
    };

class AffineTransform {
private:
    double ap;
    double bp;
    double cp;
    double dp;
    double ep;
    double fp;
    Point coor;

public:
    AffineTransform(double a, double b, double c, double d, double e = 0, double f = 0) {
        ap = a;
        bp = b;
        cp = c;
        dp = d;
        ep = e;
        fp = f;
    }

    void calc(Point coor) {
        double X = ap*coor.x + bp*coor.y + ep;
        double Y = cp*coor.x + dp*coor.y + fp;
        cout << "x = " << X << endl;
        cout << "y = " << Y << endl;
    }
};


int main() {
    AffineTransform AT(1,1,1,1);
    struct Point p1 = {4,3};
    AT.calc(p1);
    return 0;
}