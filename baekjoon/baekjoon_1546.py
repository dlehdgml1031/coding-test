n = int(input())
score_list = list(map(int, input().split()))

max_score = max(score_list)
new_score_list = [x / max_score * 100 for x in score_list]

print(sum(new_score_list) / len(new_score_list))