import sys 
from collections import deque
input = sys.stdin.readline 

t = int(input()) # 테스트케이스 수 

def bfs(start):
    queue = deque()

    queue.append(start)

    while queue:
        start = queue.popleft()

        # 바로 락 페스티벌에 갈 수 있으면 끝
        if abs(end[0]-start[0]) + abs(end[1]-start[1]) <= 1000: 
            return 'happy'

        else:
            for s in range(len(store)):
                dist = abs(store[s][0]-start[0]) + abs(store[s][1]-start[1])

                if not visited[s] and dist <= 1000:
                    visited[s] = True # 방문처리 
                    queue.append(store[s]) # queue에 저장 
    else:
        return 'sad'


for _ in range(t):
    n = int(input()) # 편의점 개수 
    store = []
    for i in range(n+2):
        if i == 0:
            start = [*map(int, input().split())] # 상근이네 집 위치(시작)
        elif i == n+1:
            end = [*map(int, input().split())] # 락 페스티벌 위치(도착)
        else:
            store.append([*map(int, input().split())])
    
    visited = [False]*len(store)

    print(bfs(start))
             