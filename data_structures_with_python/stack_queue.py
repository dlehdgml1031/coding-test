from dataclasses import dataclass

# Stack class
@dataclass
class Stack:
    items = []
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0
    

def parChecker(parSeq: str):
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
    
@dataclass
class PostfixCalc:
    expr: str
    operator_list:list = ['+', '-', '*', '/', '^']
    
    def get_token_list(self) -> list:
        return None
    
    def infix_to_postfix(token_list):
        return None
    
    def compute_postfix(token_list):
        return None
    

if __name__ == '__main__':
    calc = PostfixCalc('(1 + 2) *3')
    print(calc.get_token_list())