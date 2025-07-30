#include <bits/stdc++.h>
using namespace std;

int n;
double sum = 0, avg = 0;

int main() {
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // 정렬 - vector만 가능
    sort(a.begin(), a.end());
    
    // Avg
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }
    avg = sum / n;

    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }

    cout << fixed << setprecision(2) << avg << "\n";

    return 0;
}