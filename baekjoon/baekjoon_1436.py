# N <= 10_000 자연수
N = int(input())
count = 0
temp_num = 0
start_num = 0

while count < N:
    if '666' in str(start_num):
        if start_num != temp_num:
            temp_num = start_num
            count += 1
    
    start_num += 1
    
print(temp_num)