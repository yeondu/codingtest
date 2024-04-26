from collections import deque

num = int(input())

num = deque(range(1, num+1))

while len(num) != 1:
    num.popleft() # 가장 첫번째 숫자 제거 

    # 그 다음 위에 있는 숫자 마지막으로 옮김 
    num.append(num.popleft())

print(num[0])