from collections import deque

sentences = []
while True:
    s = input()
    if s == '.':
        break
    sentences.append(s)

for s in sentences:
    st = deque()
    balanced = True
    
    for c in s:
        if c in '([':
            st.append(c)
        elif c == ')':
            if not st or st.pop() != '(':
                balanced = False
                break
        elif c == ']':
            if not st or st.pop() != '[':
                balanced = False
                break
            
    if balanced and not st:
        print("yes")
    else:
        print("no")