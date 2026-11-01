# 모의고사
# LV1

from collections import deque, defaultdict

def solution(answers):
    ans_arr = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]        
    ]
    
    res = [[0] * (len(answers) + 1) for _ in range(3)]
    
    for idx, n in answers:
        for i in range(3):
            if n == ans_arr[i][idx%len(ans_arr[i])]:
                res[i][idx + 1] = res[i][idx] + 1
            else:
                res[i][idx + 1]= res[i][idx]
    
    ans_dict = defaultdict(int)
    
    for i in range(3):
        ans_dict[i] = res[i][-1]
        
    ans_dict = sorted(ans_dict, key = lambda x: x)
    
    print(ans_dict)
    
    return 0