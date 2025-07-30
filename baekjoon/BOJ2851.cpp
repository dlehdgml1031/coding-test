#include <iostream>
#include <cmath>
using namespace std;

int mushrooms[10], score = 0;

int main() {
    for (int i = 0; i < 10; i++) {
        cin >> mushrooms[i];
    }

    for (int i = 0; i < 10; i++) {
        if ((abs(100 - score)) >= abs(100 - (score + mushrooms[i]))) {
            score += mushrooms[i];
        } else {
            break;
        }
    }
    cout << score << "\n";
    return 0;
}