
class Stack:
    def __init__(self):
        self.items:list = []
    
    def push(self, X):
        return self.items.append(X)
    
    def pop(self):
        if len(self.items) == 0:
            print(-1)
        else:
            print(self.items[-1])
            return self.items.pop()
    
    def size(self):
        print(len(self.items))
    
    def empty(self):
        print(1) if len(self.items) == 0 else print(0)    
    
    def top(self):
        print(-1) if len(self.items) == 0 else print(self.items[-1])

def main():
    n = int(input())
    input_list = [input().split() for _ in range(n)]
    s = Stack()
    
    for i in input_list:
        func_name = i[0]
        if len(i) == 2:
            X = i[1]
        
        if func_name == 'push':
            s.push(X)
        elif func_name == 'pop':
            s.pop()
        elif func_name == 'size':
            s.size()
        elif func_name == 'empty':
            s.empty()
        elif func_name == 'top':
            s.top()

if __name__ == '__main__':
    main()