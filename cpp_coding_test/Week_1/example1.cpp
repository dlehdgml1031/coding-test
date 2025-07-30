// #include <iosteram>
// #include <algorithm>
// #include <string>
#include <bits/stdc++.h>
using namespace std;

string dopa = "umzunsik";

int main() {
    // Q1) 앞에서부터 3개의 문자열을 출력
    cout << dopa.substr(0,3) << "\n";

    // Q2) 해당 문자열을 거꾸로 해서 출력
    reverse(dopa.begin(), dopa.end());
    cout << dopa << "\n";

    // Q3) 거꾸로된 해당 문자열 끝에 "umzunsik" 문자열 추가
    dopa += "umzunsik";
    cout << dopa << "\n";

    return 0;
}