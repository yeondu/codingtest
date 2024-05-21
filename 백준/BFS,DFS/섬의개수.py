import sys 
sys.setrecursionlimit(10**6)
w, h = map(int, input().split())

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def dfs(x, y):
    visited[x][y] = True 
    for s in range(8):
        nx = x + dx[s] 
        ny = y + dy[s]

        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)

while w != 0 and h != 0:
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                count += 1 
                dfs(i, j)

    print(count)
    w, h = map(int, input().split())
