#include <bits/stdc++.h>
using namespace std;

int n = 5, k = 3;
int a[5] = {1, 2, 3, 4, 5};

int main()
{
    // version 1 - j < n / 
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            for (int k = j + 1; k < n; k++)
            {
                cout << i << " " << j << " " << k << "\n";
            }
        }
    }

    cout << "\n\n";
    // version 2 - i < n / j < i / k < j
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            for (int k = 0; k < j; k++)
            {
                cout << i << " " << j << " " << k << "\n";
            }
        }
    }


    return 0;
}