#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

bool reportSafe(vector<int> input) {
  int direction = input[1] - input[0];
  for (int i = 0; i < input.size() - 1; i++) {
    if (abs(input[i + 1] - input[i]) > 3 || abs(input[i + 1] - input[i]) == 0 ||
        (input[i + 1] - input[i]) * direction < 0)
      return false;
  }
  return true;
}

int main() {
  ifstream file("input.txt");
  string line;
  vector<int> report;
  istringstream stream;
  int elt, sum = 0;

  while (getline(file, line)) {
    stream.str(line);
    stream.clear();
    while (stream >> elt)
      report.push_back(elt);
    if (reportSafe(report))
      sum++;
    report.clear();
  }
  cout << sum;
}
