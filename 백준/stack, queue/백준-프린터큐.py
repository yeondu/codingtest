# 첫번째 줄은 테스트케이스의 수 

import sys 
input = sys.stdin.readline 

num = int(input()) # 총 테스트케이스 개수 

# 1 0 => 문서의 개수는 1개, 우리가 찾아야 할 문서가 몇번째에 놓여있는지 
# 문서의 개수는 1개이고, 우리가 찾고자 하는 문서는 0번째에 놓여있음
# 그 다음은 문서의 중요도가 차례로 주어짐
# 5이고 문서의 개수가 1개니까 중요도가 5인 문서가 1개 존재 => 가장 먼저 출력 

from collections import deque
for _ in range(num):
    result = 0
    n, m = list(map(int, input().strip().split()))
    # 문서 데이터 
    file = deque(list(map(int, input().strip().split())))
    # 계속 뒤로 빼다가 맨 앞에 있는게 가장 큰 수면 빼고 횟수 +1 
    # 인덱스도 변경 
    while m != -1:
        if file[0] != max(file):
            if m != 0:
                file.append(file.popleft())
                m -= 1
            else:
                file.append(file.popleft())
                m = len(file)-1 # 맨 뒤 인덱스로 변경 

        else:
            if m != 0:
                file.popleft()
                result += 1 
                m -= 1


            else:
                result += 1
                m = -1

    print(result)

        
