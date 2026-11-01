from collections import deque, Counter, defaultdict

def solution(numbers, target):
    N = len(numbers)
        
    def dfs(depth, total):
        # Base Rule
        if depth == N:
            return 1 if total == target else 0
        
        res = 0
        for sign in (1, -1):
            res += dfs(depth + 1, total + sign * numbers[depth])
        return res
            
    return dfs(0,0)