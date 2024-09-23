#include <iostream>
#include <vector>
using namespace std;

struct Node {
  int value;
  Node *next;
  Node *previous;

  Node(int n) {
    value = n;
    next = nullptr;
    previous = nullptr;
  }
  Node(int n, Node *p) {
    value = n;
    previous = p;
    next = nullptr;
  }
};

class LinkedList {
private:
  Node *head;
  Node *tail;
  Node *get_node(int index) {
    if (index < 0 or index >= size) {
      throw range_error("IndexError: Index out of range");
    }

    Node *current = head;
    for (int i = 0; i < index; i++) {
      current = current->next;
    }
    return current;
  }

public:
  int size;
  LinkedList() {
    size = 0;
    head = nullptr;
    tail = nullptr;
  }
  ~LinkedList() {
    Node *current;
    Node *next;

    current = head;

    while (current != nullptr) {
      next = current->next;
      delete current;
      current = next;
    }
  }
  LinkedList(vector<int> vec) {
    size = 0;
    head = nullptr;
    tail = nullptr;

    for (int e : vec) {
      append(e);
    }
  }

  int length() { return size; }

  void append(int val) {
    if (head == nullptr) {
      head = new Node(val);
      tail = head;
      size++;
      return;
    } else {
      Node *current = tail;

      tail = new Node(val, current);
      current->next = tail;

      size++;
      return;
    }
  }
  void print() {
    Node *current = head;
    cout << "[";
    while (current->next != nullptr) {
      cout << current->value;
      cout << ", ";
      current = current->next;
    }
    cout << current->value << "]" << endl;
  }

  int &operator[](int index) { return get_node(index)->value; }

  void insert(int val, int index) {

    if (index == 0) {
      Node *newhead = new Node(val);
      Node *oldhead = head;

      oldhead->previous = newhead;
      newhead->next = oldhead;
      head = newhead;

      size++;
      return;
    }

    Node *oldnode = get_node(index - 1);
    Node *next = oldnode->next;
    Node *newnode = new Node(val, oldnode);

    newnode->next = next;
    oldnode->next = newnode;
    next->previous = newnode;

    size++;
  }

  void remove(int index) {
    if (index == 0) {
      Node *next = head->next;
      head->next = nullptr;

      next->previous = nullptr;

      head = next;

      size -= 1;
      return;
    }

    if (index == size - 1) {
      Node *previous = tail->previous;
      tail->previous = nullptr;

      previous->next = nullptr;

      tail = previous;
      size -= 1;
      return;
    }

    Node *oldnode = get_node(index);
    Node *next = oldnode->next;
    Node *previous = oldnode->previous;

    next->previous = previous;
    previous->next = next;

    size -= 1;
  }

  int pop(int index) {
    int element = get_node(index)->value;
    remove(index);
    return element;
  }

  int pop() {
    int element = tail->value;
    remove(size - 1);
    return element;
  }
};

int main() {
  LinkedList Example;
  cout << "Appending 2, 3, 7, 9, 11, 14" << endl;
  Example.append(2);
  Example.append(3);
  Example.append(7);
  Example.append(9);
  Example.append(11);
  Example.append(14);
  Example.print();

  cout << "Insert 1 at front, 5 in index 3, 13 at index 7" << endl;
  Example.insert(1, 0);
  Example.insert(5, 3);
  Example.insert(13, 7);
  Example.print();

  cout << "The 4th element is: " << Example[3] << endl;

  cout << "Remove the 6th element" << endl;
  Example.remove(5);
  Example.print();

  cout << "Removing: " << Example.pop(0) << endl;
  Example.print();

  cout << "Removing: " << Example.pop() << endl;
  Example.print();

  cout << "Testing overloaded constructor" << endl;
  LinkedList VecList({0, 2, 4, 6, 8, 10});
  VecList.print();

  return 0;
}
