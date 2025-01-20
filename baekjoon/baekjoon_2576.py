input_list = [int(input()) for _ in range(7)]
res_list = []

for i in input_list:
    if i % 2 != 0:
       res_list.append(i)

if len(res_list) == 0:
    print(-1)
else:
    print(sum(res_list))
    print(min(res_list))