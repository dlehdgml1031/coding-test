n, m = map(int, (input().split()))
m_list = list(map(int, (input().split())))

res_list = []

for i in m_list:
    for j in m_list:
        for k in m_list:
            if i == j == k or i == j or j == k or i == k:
                continue
            
            if i + j + k <= m:
                res_list.append(i + j + k)

print(max(res_list))