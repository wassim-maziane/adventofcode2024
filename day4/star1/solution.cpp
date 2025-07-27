#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  ifstream file("input.txt");
  string line;
  vector<string> lines;
  while (getline(file, line)) {
    lines.push_back(line);
  }
  file.close();
}
