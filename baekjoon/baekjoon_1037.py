num_factors = int(input())
factors_input = input().split()
factors_list = [int(i) for i in factors_input]

if num_factors == 1:
    print(factors_list[0] ** 2)
else:
    factors_list.sort()
    print(factors_list[0] * factors_list[-1])