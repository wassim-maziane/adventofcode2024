#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

bool reportSafe(vector<int> input) {
  int direction = input[1] - input[0];
  int anomalyCounter = 0;
  int n = input.size();
  for (int i = 0; i < n - 1; i++) {
    if (abs(input[i + 1] - input[i]) > 3 || abs(input[i + 1] - input[i]) == 0 ||
        (input[i + 1] - input[i]) * direction < 0) {
      input.erase(input.begin() + i);
      anomalyCounter++;
      n--;
      i--;
    }
    if (anomalyCounter > 1)
      return false;
  }
  return true;
}

int main() {
  ifstream file("test_salah.txt");
  string line;
  vector<int> report;
  istringstream stream;
  int elt, sum = 0;
  int report_number = 0;

  while (getline(file, line)) {
    stream.str(line);
    stream.clear();
    while (stream >> elt)
      report.push_back(elt);
    report_number++;
    if (reportSafe(report)) {
      cout << report_number << " " << reportSafe(report) << '\n';
      sum++;
    }
    report.clear();
  }
  cout << sum;
}
