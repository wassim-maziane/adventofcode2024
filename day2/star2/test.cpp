#include <iostream>
#include <vector>
using namespace std;
int reportSafe(vector<int> input) {
  int direction = input[1] - input[0];
  int anomalyCounter = 0;
  int n = input.size();
  for (int i = 0; i < n - 1; i++) {
    if (abs(input[i + 1] - input[i]) > 3 || abs(input[i + 1] - input[i]) == 0 ||
        (input[i + 1] - input[i]) * direction < 0) {
      input.erase(input.begin() + i + 1);
      anomalyCounter++;
      n--;
      i--;
    }
  }
  return anomalyCounter;
}

int main() {
  vector<int> test = {38, 40, 43, 44, 44};
  cout << reportSafe(test);
}
