#include <iostream>
#include <cmath>

using namespace std;

const double pi = 3.14159265359;

struct Cartesian {
    double x;
    double y;
};

struct Polar {
    double r;
    double theta;
};

void cart2polar(Cartesian cart) {
    double r = sqrt(cart.x*cart.x + cart.y*cart.y);
    double theta = atan(cart.y/cart.x);
    cout << "r = " << r << endl;
    cout << "theta = " << theta << endl;
}

void polar2cart(Polar pol) {
    double x = pol.r*cos(pol.theta);
    double y = pol.r*sin(pol.theta);
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
}

void scalar(Polar coor, double s) {
    double scalar_r = coor.r*s;
    cout << "r = " << scalar_r << endl;
    cout << "theta = " << coor.theta << endl;
}

void scalar(Cartesian coor, double s) {
    double scalar_x = coor.x*s;
    double scalar_y = coor.x*s;
    
    cout << "x = " << scalar_x << endl;
    cout << "y = " << scalar_y << endl;
}

void rotate(Polar coor, double omega) {
    double theta = coor.theta + omega;
    cout << "r = " << coor.r << endl;
    cout << "theta = " << theta << endl;
}

void rotate(Cartesian coor, double omega) {
    double x = cos(omega)*coor.x - sin(omega)*coor.y;
    double y = sin(omega)*coor.x + cos(omega)*coor.y;
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
}

int main() {
    struct Cartesian cart = {1,1};
    struct Polar pol = {4,pi/6};
    cart2polar(cart);
    polar2cart(pol);
    rotate(cart, 5);
    return 0;
}