n = int(input())
word_list = [input().strip() for _ in range(n)]
count_num = 0

for word in word_list:
    temp_unique_char = set([x.strip() for x in word])
    flag = 1
    
    for char in temp_unique_char:
        if word.count(char) == 1:
            continue
        
        if len(word[word.find(char) : word.rfind(char) + 1]) != word.count(char):
            flag = 0
    
    if flag:
        count_num += 1

print(count_num)