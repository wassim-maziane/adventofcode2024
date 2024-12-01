#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
  ifstream file("input.txt");
  string line;
  istringstream stream;
  int n1, n2;
  int similary_search_score = 0;
  vector<int> L1, L2;
  unordered_map<int, int> counter;

  while (getline(file, line)) {
    stream.str(line);
    stream.clear();
    stream >> n1 >> n2;
    L1.push_back(n1);
    L2.push_back(n2);
  }
  // L1 = {3, 4, 2, 1, 3, 3};
  // L2 = {4, 3, 5, 3, 9, 3};
  for (int elt : L2)
    counter[elt]++;
  for (int elt : L1) {
    // cout << elt << ' ' << counter[elt] << '\n';
    similary_search_score += elt * counter[elt];
  }
  cout << similary_search_score;
}
