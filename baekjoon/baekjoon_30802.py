n = int(input())
t_list = [int(x) for x in input().split()]
t, p = map(int, input().split())
t_ord_num = 0

for i in t_list:
    if i > t:
        if ((i % t) == 0):
            t_ord_num += (i // t)
        else:
            t_ord_num += ((i // t) + 1)
    elif i == 0:
        continue
    else:
        t_ord_num += 1

print(t_ord_num)
print(n // p, n % p)