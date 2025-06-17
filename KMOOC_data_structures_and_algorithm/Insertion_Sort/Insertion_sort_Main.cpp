#include <iostream>
#include <vector>

template <typename Type>
void Insertion_Sort(Type *_array, int _n)
{
    for(int i = 1; i < _n; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (_array[j-1] > _array[j])
            {
                std::swap(_array[j-1], _array[j]);
            }
            else
            {
                break;
            }
        }
    }
}

template <typename Type>
void Insertion_Sort_without_Swap(Type *_array, int _n)
{
    for (int i = 1; i < _n; i++)
    {
        Type tmp = _array[i];
        for (int j = i; j > 0; j--)
        {
            if (_array[j-1] > tmp)
            {
                _array[j] = _array[j - 1];
            }
            else
            {
                _array[j] = tmp;
                break;
            }
        }
        if ( _array[0] > tmp )
        {
            _array[0] = tmp;
        }
    }
}

int main()
{
    // 정수 배열 예시
    int intArr[] = {5,2,9,1,5,6};
    int nInt = sizeof(intArr) / sizeof(intArr[0]);

    std::cout << "정렬 전 (int): ";
    for (int i = 0; i < nInt; ++i)
        std::cout << intArr[i] << ' ';
    std::cout << '\n';

    // 정렬 수행
    Insertion_Sort(intArr, nInt);

    std::cout << "정렬 후 (int): ";
    for (int i = 0; i < nInt; ++i)
        std::cout << intArr[i] << ' ';
    std::cout << "\n\n";

    return 1;
}