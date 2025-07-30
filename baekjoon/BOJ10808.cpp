#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string s;

int main() {
    cin >> s;

    for (int i = (int)'a'; i <= (int)'z'; i++) {
        int cnt = 0;
        for (char a : s) {
            if (a == (char)i)
                cnt += 1;
        }
        cout << cnt << " ";
    }

    return 0;
}