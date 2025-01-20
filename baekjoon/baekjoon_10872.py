# num = int(input())

# def factorial(input_num):
#     if input_num == 0:
#         return 1
    
#     init_num = 1
#     for i in range(1, input_num + 1):
#         init_num = init_num * i
    
#     return init_num

# a = factorial(num)
# print(a)


### for 문 풀이 ###
n = int(input())

res = 1
if n > 0:
    for i in range(1, n +1):
        res *= i

print(res)