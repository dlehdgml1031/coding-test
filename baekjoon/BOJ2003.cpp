#include <iostream>
using namespace std;

 int n, m, a[10000], cnt = 0;

 int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    for (int i = 0; i < n; i++) {
        int score = 0;
        for (int j = i; j < n; j++) {
            score += a[j];
            if (score == m) {
                cnt++;
                break;
            }
        }
    }

    cout << cnt << "\n";

    return 0;
 }