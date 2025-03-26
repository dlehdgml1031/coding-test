class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, value):
        return self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is empty')
    
    def isEmpty(self):
        return len(self.items) == 0

def parChecker(parSeq:str):
    S = Stack()
    
    for symbol in parSeq:
        if symbol == "(":
            S.push(symbol)
        elif symbol == ")":
            if S.isEmpty():
                return False
            else:
                S.pop()
        else:
            continue
        
    if S.isEmpty():
        return True
    else:
        return False


n = int(input())
parSeqList = [input() for _ in range(n)]

for parSeq in parSeqList:
    print("YES") if parChecker(parSeq) else print("NO")