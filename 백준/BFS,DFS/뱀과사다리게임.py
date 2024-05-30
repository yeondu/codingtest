import sys 
from collections import deque
input = sys.stdin.readline 

n, m = map(int, input().split())
up = {}
down = {}

for _ in range(n):
    start, end = map(int, input().split()) # 사다리의 시작과 도착 위치 
    up[start] = end # 딕셔너리 사용해서 위치값 저장 . 
    # 하다가 이게 안되면 리스트로 시작위치랑 도착위치 별도 리스트로 묶어서 진행

for _ in range(m):
    start, end = map(int, input().split())
    down[start] = end 

game = [100] * 101

# 시작위치는 1 

dice = [1,2,3,4,5,6]

def bfs():
    queue = deque()
    queue.append(1) # 시작위치 
    game[1] = 0

    while queue:
        x = queue.popleft() # 시작위치 추출 
        for i in dice: # 주사위의 위치를 한번 다 돎 
            if x+i <= 100:
                if game[x+i] > game[x]+1:
                    game[x+i] = game[x]+1 

                # 다음걸 갱신하는건 어떤거에 해당해도 무조건 되니까 
                    if x+i in up.keys():
                        # 도착 위치의 이동 횟수 max 활용해서 갱신 
                        game[up[x+i]] = min(game[up[x+i]], game[x+i]) # 사다리로 이동한 위치 값도 변경
                        # 이미 game[x+i]를 갱신했으니가 해당 값이랑 비교하면 됨. 
                        # 그러고 그 다음 이동 위치를 queue에 저장 
                        if up[x+i] not in queue:
                            queue.append(up[x+i])
                    elif x+i in down.keys():
                        game[down[x+i]] = min(game[down[x+i]], game[x+i])
                        if down[x+i] not in queue:
                            queue.append(down[x+i])
                    else: # 사다리와 뱀이 없는 경우
                        # 다 저장하지 말고 queue에 없는 것만 저장
                        if x+i not in queue:
                            queue.append(x+i)

    print(game[100])

bfs()

    
