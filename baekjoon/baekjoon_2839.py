n = int(input())
total_num_list = []

# 5의 배수
for i in range(1, (5000 // 5) + 1):
    if (n < 5 * i):
        break
    
    if n % (5 * i) == 0:
        total_num_list.append(n // (5 * i))
        continue
    
    for j in range(1, round(5000 // 3)):
        if (n - (5 * i)) < (3 * j):
            break
        
        if (n - (5 * i)) % (3 * j) == 0:
            total_num_list.append(
                i + ((n - (5 * i)) // (3 * j))
            )


# for i in range(1, round(5000 // 3)):
#     if (3 * i > n):
#         break
    
#     for j in range(1, (5000 // 5) + 1):
#         if (5 * j > (n % (3 * i))):
#             break
        
#         if ((n % (5 * i)) % (3 * j)) == 0:
#             total_num_list.append((n // (3 * i)) + ((n % (3 * i)) // (5 * j)))


print(min(total_num_list))