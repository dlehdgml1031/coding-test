n, m = map(int, input().split())
board_stat = [input().strip() for _ in range(n)]

answer_dict = {
    'B' : 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB',
    'W' : 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
}

count_list = []

for row_start_idx in range(n - 7):
    temp_row_list = board_stat[row_start_idx : row_start_idx + 8]
    
    for col_start_idx in range(m - 7):
        temp_line = ''
        
        for line in temp_row_list:
            temp_line += line[col_start_idx : col_start_idx + 8]
        
        
        temp_count = 0
        for current_board_color, answer_board_color in zip(temp_line, answer_dict['B']):
                    if current_board_color != answer_board_color:
                        temp_count += 1
        count_list.append(temp_count)
        
        
        temp_count = 0
        for current_board_color, answer_board_color in zip(temp_line, answer_dict['W']):
                if current_board_color != answer_board_color:
                        temp_count += 1
        count_list.append(temp_count)

print(min(count_list))


################################ 다른 사람 풀이 ################################


