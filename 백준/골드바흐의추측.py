import sys 
input = sys.stdin.readline 
from collections import deque 

t = int(input())

# 소수 리스트 생성 
num_list = deque(i for i in range(2,10001))
prime_list  = []

while num_list:
    num = num_list.popleft()
    prime_list.append(num)
    num_list = deque(i for i in num_list if i%num != 0) # 2의 배수 제거 


for _ in range(t):
    n = int(input())
    if n//2 in prime_list: # 몫이 소수 리스트에 포함되어 있으면 해당 값 두번 나온게 정답 
        print(f'{n//2} {n//2}')
    else:
        count = 0 
        for p in prime_list:
            if abs(n-p) in prime_list:
                if count == 0:
                    a, b, count = p, abs(n-p), abs(n-p-p)
                elif count > abs(n-p-p):
                    a, b, count = p, abs(n-p), abs(n-p-p)
        print(f'{a} {b}')
