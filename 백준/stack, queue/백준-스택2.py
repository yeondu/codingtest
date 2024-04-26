stack = []
import sys 

input = sys.stdin.readline 
num = int(input()) # 초기 값 받음

for i in range(num):
    # sys.stdin.readline을 사용하면 불러올 때 개행문자(\n) 없애야함
    data = list(map(int, input().rstrip().split(' ')))
    #data = input().split() # 이렇게 사용하면 리스트로 묶여서 바로바로 들어가긴 함
    # 개행문자 제거도 필요없고 리스트로 지정도 안해줘도 됨(대신 int로 나오지 않으니 이 부분만 수정하면 됨)
    print(data)
    if data[0] == 1:
        stack.append(data[1])
    elif data[0] == 2:
        if not stack:
            print(-1)
        else:
            p_num = stack[-1]
            stack.pop()
            print(p_num)
    elif data[0] == 3:
        print(len(stack))
    elif data[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif data[0] == 5:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
