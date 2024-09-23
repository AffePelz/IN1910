#include <cmath>
#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

class ArrayList {
private:
  int capacity;
  int *data;

  void resize() {
    capacity *= 2;
    int *tmp = new int[capacity];
    for (int i = 0; i < size; i++) {
      tmp[i] = data[i];
    }
    delete[] data;
    data = tmp;
  }

public:
  int size;
  ArrayList() {
    size = 0;
    capacity = 1;
    data = new int[capacity];
  }
  ArrayList(vector<int> vec) {
    size = 0;
    capacity = 1;
    data = new int[capacity];

    for (int e : vec) {
      append(e);
    }
  }
  ~ArrayList() { delete[] data; }
  int length() { return size; }
  void append(int n) {
    if (size >= capacity) {
      resize();
    }
    data[size] = n;
    size += 1;
  }
  void print() {
    cout << "[";
    for (int i = 0; i < size - 1; i++) {
      cout << data[i];
      cout << ", ";
    }
    cout << data[size - 1] << "]" << endl;
  }

  int &operator[](int i) {
    if (0 <= i and i < size) {
      return data[i];
    } else {
      throw out_of_range("IndexError");
    }
  }

  void insert(int val, int index) {
    if (index > size) {
      throw out_of_range("IndexError");
    }
    capacity += 1;
    size += 1;
    int *tmp = new int[capacity];
    for (int i = 0; i < index; i++) {
      tmp[i] = data[i];
    }
    tmp[index] = val;
    for (int i = index; i < size; i++) {
      tmp[i + 1] = data[i];
    }
    delete[] data;
    data = tmp;
  }

  void remove(int index) {
    size -= 1;
    int *tmp = new int[capacity];
    for (int i = 0; i < index; i++) {
      tmp[i] = data[i];
    }
    for (int i = index; i < size; i++) {
      tmp[i] = data[i + 1];
    }
    delete[] data;
    data = tmp;
    if (size / capacity < 0.25) {
      shrink_to_fit();
    }
  }

  int pop(int index) {
    int element = data[index];
    remove(index);
    return element;
  }

  int pop() {
    int element = data[size - 1];
    remove(size - 1);
    return element;
  }

  void shrink_to_fit() {
    int n = ceil(log2(size));
    capacity = pow(2, n);
  }
};

bool is_prime(int n) {
  if (n == 1) {
    return false;
  } else if (n < 4) {
    return true;
  } else if (n % 2 == 0 || n % 3 == 0) {
    return false;
  }

  for (int i = 5; i <= sqrt(n); i = i + 6) {
    if (n % (i) == 0 || n % (i + 2) == 0) {
      return false;
    }
  }
  return true;
}

void test_is_prime() {
  ArrayList Primes;
  int n = 2;
  while (Primes.length() < 10) {
    if (is_prime(n) == true) {
      Primes.append(n);
    }
    n += 1;
  }

  Primes.print();
}

int main() {

  ArrayList primes({2, 3, 5, 8, 11});
  primes.print();

  // test_is_prime();
  return 0;
}
