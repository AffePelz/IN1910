#include <iostream>
#include <vector>

using namespace std;

struct Node {
  int value;
  Node *next;

  Node(int n) {
    value = n;
    next = nullptr;
  }
  Node(int n, Node *p) {
    value = n;
    next = p;
  }
};

class CircLinkedList {
private:
  Node *head;
  Node *tail;
  Node *get_node(int index) {
    Node *current = head;
    for (int i = 0; i < index; i++) {
      current = current->next;
    }
    return current;
  }

public:
  int size;
  CircLinkedList() {
    size = 0;
    head = nullptr;
    tail = head;
  }

  CircLinkedList(int n) {
    size = 0;
    head = nullptr;
    tail = head;
    for (int i = 1; i <= n; i++) {
      append(i);
    }
  }

  vector<int> josephus_sequence(int k) {
    vector<int> dead;
    int i = 0;

    Node *leftnode = get_node(k - 2);
    Node *rightnode = leftnode->next;

    while (size > 1) {

      leftnode->next = rightnode->next;
      rightnode->next = nullptr;

      dead.push_back(rightnode->value);
      size -= 1;

      for (int j = 1; j < k; j++) {
        leftnode = leftnode->next;
      }
      rightnode = leftnode->next;
      i++;
    }
    dead.push_back(leftnode->value);
    return dead;
  }

  void append(int val) {
    if (head == nullptr) {
      head = new Node(val);
      tail = head;
      tail->next = head;
      size++;
      return;
    }

    // Iterate to end of list
    Node *newnode = new Node(val, head);
    tail->next = newnode;
    tail = newnode;
    size++;
  }

  int &operator[](int index) {
    if (head == nullptr) {
      throw out_of_range("IndexError");
    }
    return get_node(index)->value;
  }

  void print() {
    Node *current = head;
    cout << "[";
    for (int i = 0; i < size; i++) {
      cout << current->value;
      cout << ", ";
      current = current->next;
    }
    cout << "..."
         << "]" << endl;
  }
};

int last_man_standing(int n, int k) {
  CircLinkedList Josephus(n);
  vector<int> dead_vector = Josephus.josephus_sequence(k);
  return dead_vector[n - 1];
}

int main() {
  CircLinkedList clist;
  clist.append(0);
  clist.append(2);
  clist.append(4);
  clist.print();

  cout << "Last man standing is man number ";
  cout << last_man_standing(68, 7) << endl;
  return 0;
}
