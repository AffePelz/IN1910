#include <iostream>
#include <vector>

using namespace std;

vector<double> find_primes(double nr, double nrk, double N=50) {
	vector<double> primes;

    double delta = (nrk - nr)/(N - 1);
	for (int i = 0; i < nrk; i++) {
        double m = nr + i*delta;
        if (m <= nrk) {
            primes.push_back(m);
        }
	}
	return primes;
}

int main() {
	vector<double> primes = find_primes(0,70);

	for (double p: primes) {
		cout << p << endl;
	}

	return 0;
}