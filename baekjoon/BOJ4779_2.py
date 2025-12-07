# Solve 2: Recursive Function (Top-down)
# func(k): k일 때의 답을 출력하는 함수
# func(k) = func(k-1) + 공백 3**(k-1) + func(k-1)

def func(k):
    # Base Case
    if k == 0:
        print('-', end = "")
        return
    
    # Recursive Case
    func(k-1)
    print(' ' * (3 ** (k-1)), end = "")
    func(k-1)

while True:
    try:
        N = int(input())
        func(N)
        print()
    except:
        break
     