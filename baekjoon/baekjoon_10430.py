# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
input_list = [int(i) for i in input().split()]
a = input_list[0]
b = input_list[1]
c = input_list[-1]

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
