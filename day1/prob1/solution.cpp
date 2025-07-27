#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
  string line;
  vector<int> L1, L2;
  ifstream file("input.txt");
  int output = 0;
  istringstream stream;

  while (getline(file, line)) {
    stream.str(line);
    stream.clear();
    int n1, n2;
    stream >> n1 >> n2;
    L1.push_back(n1);
    L2.push_back(n2);
  }
  sort(L1.begin(), L1.end());
  sort(L2.begin(), L2.end());
  for (int i = 0; i < L1.size(); i++)
    output += abs(L1[i] - L2[i]);
  cout << output;
  file.close();
}
