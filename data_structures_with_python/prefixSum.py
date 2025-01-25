# ### 문제 1 ###
import time, random

def prefixSum1(X, n):
    S = [0 for _ in range(n)]
    for i in range(n):
        temp_s = 0
        
        for j in range(i):
            temp_s += X[j]
        
        S[i] = temp_s

def prefixSum2(X, n):
    S = [0 for _ in range(n)]
    S[0] = X[0]
    
    for i in range(1, n):
        S[i] = S[i-1] + X[i]


random.seed()
n = int(input())
X = [random.randint(-999,999) for _ in range(n)]

# 실행시간 : 3.132
before = time.process_time()
prefixSum1(X = X, n = n)
after = time.process_time()
print(after - before)

# 실행시간 0.001371
before = time.process_time()
prefixSum2(X = X, n = n)
after = time.process_time()
print(after - before)