w1 = input().split(",")
w2 = input().split(",")

n=12000
grid = [[0 for i in range(n)] for j in range(n)]

coords = [n//2,n//2]
for path in w1:
    d = path[0]
    length = int(path[1:])
    if d=='L':
        for i in range(length):
            grid[coords[0]][coords[1]-1] = 1
            coords[1] -= 1
    elif d=='R':
        for i in range(length):
            grid[coords[0]][coords[1]+1] = 1
            coords[1] += 1
    elif d=='U':
        for i in range(length):
            grid[coords[0]-1][coords[1]] = 1
            coords[0] -= 1
    elif d=='D':
        for i in range(length):
            grid[coords[0]+1][coords[1]] = 1
            coords[0] += 1
            
coords = [n//2,n//2]
for path in w2:
    d = path[0]
    length = int(path[1:])
    if d=='L':
        for i in range(length):
            if grid[coords[0]][coords[1]-1] == 1:
                grid[coords[0]][coords[1]-1] += 1
            coords[1] -= 1
    elif d=='R':
        for i in range(length):
            if grid[coords[0]][coords[1]+1] == 1:
                grid[coords[0]][coords[1]+1] += 1
            coords[1] += 1
    elif d=='U':
        for i in range(length):
            if grid[coords[0]-1][coords[1]] == 1:
                grid[coords[0]-1][coords[1]] += 1
            coords[0] -= 1
    elif d=='D':
        for i in range(length):
            if grid[coords[0]+1][coords[1]] == 1:
                grid[coords[0]+1][coords[1]] += 1
            coords[0] += 1
           
diff = 2*n
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            temp = abs(n//2-i) + abs(n//2-j)
            diff = min(temp, diff)
        
print(diff)
        
        
        
        
        
        