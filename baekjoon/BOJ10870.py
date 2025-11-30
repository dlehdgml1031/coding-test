import sys

def fibonacci(n):
    # Base Case
    if n <= 1:
        return n
    
    # Return Case
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = int(input())
    res = fibonacci(n)
    print(res)