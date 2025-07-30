#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int a, b, c, sum = 0;
int times[100] = {0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> a >> b >> c;
    for (int i = 0; i < 3; i++){
        int start_idx, end_idx;
        cin >> start_idx >> end_idx;
        for (start_idx; start_idx < end_idx; start_idx++) {
            times[start_idx]++;
        }
    }
    for (int i : times) {
        if (i == 0) {
            continue;
        }
        else if (i == 1) {
            sum += a * 1;
        } 
        else if (i == 2) {
            sum += b * 2;
        }
        else{
            sum += c * 3;
        }
    }
    cout << sum;

    return 0;
}
