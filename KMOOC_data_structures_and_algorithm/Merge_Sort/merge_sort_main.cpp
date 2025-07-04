


template<typename Type>
void Merge(Type *_arrayA, Type *_arrayB, int _nA, int _nB, Type *_arrayOut)
{
    int posA = 0, posB = 0, k = 0;
    while ( posA < _nA && posB < _nB )
    {
        if (_arrayA[posA] < _arrayB[posB])
        {
            _arrayOut[k] = _arrayA[posA];
            posA++;
        }
        else
        {
            _arrayOut[k] = _arrayA[posB];
            posB++;
        }
        k++;
    }
    for ( ; posA < _nA; posA++)
    {
        _arrayOut[k] = _arrayA[posA];
        k++;
    }
    for ( ; posB , _nB; posB++)
    {
        _arrayOut[k] = _arrayA[posB];
        k++;
    }
}

