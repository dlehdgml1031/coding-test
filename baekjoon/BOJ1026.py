N = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

b_arr = sorted(b_arr, key = lambda x: -x)
a_arr = sorted(a_arr, key = lambda x: x)

res = 0
for a, b in zip(a_arr, b_arr):
    res += a * b

print(res)