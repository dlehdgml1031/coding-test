def solve():
    row_used = [set() for _ in range(9)]
    col_used = [set() for _ in range(9)]
    box_used = [set() for _ in range(9)]
    
    pos = []
    
    for i in range(9):
        for j in range(9):
            if matrix[i][j] != 0:
                num = matrix[i][j]
                row_used[i].add(num)
                col_used[j].add(num)
                box_used[(i // 3) * 3 + (j // 3)].add(num)
            else:
                pos.append((i, j))
    
    def is_possible(y, x, n):
        box_idx = (y // 3) * 3 + (x // 3)

        return n not in row_used[y] and \
               n not in col_used[x] and \
               n not in box_used[box_idx]
    
    def search(lev):
        if lev == len(pos):
            for i in range(9):
                print(' '.join(map(str, matrix[i])))
            exit(0)
        
        y, x = pos[lev]
        box_idx = (y // 3) * 3 + (x // 3)
        
        for n in range(1, 10):
            if is_possible(y, x, n):

                matrix[y][x] = n
                row_used[y].add(n)
                col_used[x].add(n)
                box_used[box_idx].add(n)
                
                search(lev + 1)
                
                matrix[y][x] = 0
                row_used[y].remove(n)
                col_used[x].remove(n)
                box_used[box_idx].remove(n)
    
    search(0)

matrix = [list(map(int, input().split())) for _ in range(9)]
solve()