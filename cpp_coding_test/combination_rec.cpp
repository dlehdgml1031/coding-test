#include <bits/stdc++.h>
using namespace std;

int n = 5, k = 4, a[5] = {1, 2, 3, 4, 5};

void print(vector <int> b)
{
    for (int i : b)
    {
        cout << i << " ";
    }
    cout << '\n';
}

void combi(int start, vector <int> &b)
{
    if (b.size() == k)
    {
        print(b);
        return;
    }
    for (int i = start + 1; i < n; i++) // idx 값이기 때문에 i < n 사용 (0,1,2,3,4 idx이기 때문)
    {
        b.push_back(i);
        combi(i, b);
        b.pop_back();
    }
    return;
}

int main()
{
    vector <int> b;
    combi(-1, b);
    return 0;
}