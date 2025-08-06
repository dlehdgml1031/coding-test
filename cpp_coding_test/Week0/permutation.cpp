#include <bits/stdc++.h>
using namespace std;

void printV(vector<int> &v)
{
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << " ";
    cout << "\n";
}

int main()
{
    // 순열을 사용하는 경우에는 vector가 정렬되어 있어야함
    int a[] = {1, 2, 3};
    vector <int> v;

    for (int i = 0; i < 3; i++)
        v.push_back(a[i]);

    // 1,2,3부터 오름차순으로 순열을 뽑음
    // vector의 경우에만 begin, end 지원
    // array의 경우에는 idx나 주소 입력
    do{
        printV(v);
    }while(next_permutation(v.begin(), v.end()));
    cout << "------------" << '\n';
    v.clear();

    // 3,2,1 내림차순으로 순열 생성
    for (int i = 2; i >= 0; i--)
        v.push_back(a[i]);
    do{
        printV(v);
    }while(prev_permutation(v.begin(), v.end()));
    
    return 0;
}