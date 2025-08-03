#include <iostream>
#include <string>
using namespace std;

string str, temp_str;

int main() {
    getline(cin, str);
    
    for (char s: str) {
        // lower Case
        if (s >= 'a' && s <= 'z') {
            temp_str += (char)('a' + (s - 'a' + 13) % 26);
        }
        // Upper Case
        else if (s >= 'A' && s <= 'Z') {
            temp_str += (char)('A' + (s - 'A' + 13) % 26);
        }
        else {
            temp_str += s;
        }
    }
    cout << temp_str << "\n";
        
    return 0;
}