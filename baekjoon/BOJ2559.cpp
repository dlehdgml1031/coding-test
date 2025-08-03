#include <iostream>
using namespace std;
int n, k, a[100004], psum[100004];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        psum[i] = psum[i - 1] + a[i];
    }
    int maxsum = psum[k];
    for (int i = k; i <= n; i++) {
        if (psum[i] - psum[i - k] >= maxsum) {
            maxsum = psum[i] - psum[i - k];
        }
    }

    cout << maxsum << "\n";

    return 0;
}