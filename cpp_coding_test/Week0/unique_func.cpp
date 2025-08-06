#include <bits/stdc++.h>
using namespace std;

map<int, int> mp;
vector<int> v2;

int main()
{
    cout << "map을 사용한 Unique" << '\n';
    vector <int> v = {1, 1, 2, 2, 3, 3};
    for (int i : v){
        if(mp[i]){
            continue;
        } else {
            mp[i] = 1;
        }
    }
    vector<int> ret;
    for (auto it : mp){
        ret.push_back(it.first);
    }
    for (int i : ret){
        cout << i << '\n';
    }

    cout << '\n' << "Unique 함수 사용" << '\n';
    for(int i = 1; i <= 5; i++){
        v2.push_back(i);
        v2.push_back(i);
    }
    for(int i : v2) cout << i << " ";
    cout << '\n';
    
    sort(v2.begin(), v2.end()); // sort 적용
    // 중복되지 않은 요소로 채운 후, 그 다음 이터레이터를 반환한다.
    v2.erase(unique(v2.begin(), v2.end()), v2.end());
    // 앞에서 부터 중복되지 않게 채운 후 나머지 요소들은 그대로 둔다.
    for(int i : v2) cout << i << " ";
    cout << '\n';

    return 0;
}

