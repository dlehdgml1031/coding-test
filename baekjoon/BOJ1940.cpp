#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int n, m, temp, ret = 0;
map<int,int> mp;

int main() {
    cin >> n;
    cin >> m;

    for (int i = 0; i < n; i++) {
        cin >> temp;
        mp[temp]++;
    }

    for (auto it : mp) {
        temp = m - it.first;

        if (mp.find(temp) != mp.end()) {
            ret++;
        }
    }

    cout << ret / 2 << "\n";

    return 0;
}