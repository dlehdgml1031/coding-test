input_str = input().upper()
original_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in input_str:
    print(original_str[original_str.index(char) - 3], end = '')