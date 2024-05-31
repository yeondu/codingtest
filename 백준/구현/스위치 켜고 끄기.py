import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n = int(input()) # 스위치 개수 

switch = list(map(int, input().split())) # 스위치 상태 

student_n = int(input()) # 학생 수 

for _ in range(student_n):
    gender, num = map(int, input().split())    

    if gender == 1: # 남학생이면 자신이 받은 수의 배수 스위치의 상태 변환
        b = n//num # 최대로 곱해질 수 있는 값 
        for i in range(1,b+1):
            if switch[(num*i)-1] == 0:
                switch[(num*i)-1] = 1
            else:
                switch[(num*i)-1] = 0
    
    else: # 여학생이면 자신이 받은 수의 스위치를 중심으로 최대 좌우대칭을 가진 범위까지 모두 상태 변환 
        # 좌우대칭인지 확인 
        left = num-2
        right = num

        # while True:
        while left >= 0 and right < n:
            if switch[left] == switch[right]:
                left -= 1 
                right += 1
            else: 
                break 


        for i in range(left+1, right):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
                
# 한 줄에 20개씩 출력 
switch = [*map(str, switch)]
start = 0 
if n <= 5: # 스위치 개수가 20개 보다 작거나 같다면 
    print(' '.join(switch[start:n]))
else: # 20개보다 많다면 
    end = 20
    while end < n: # end가 n보다 커지면 끝 
        print(' '.join(switch[start:end]))
        start += 20
        end += 20
    else:
        print(' '.join(switch[start:n]))