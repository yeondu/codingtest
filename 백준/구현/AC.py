import sys 
from collections import deque 
import re 
input = sys.stdin.readline 

n = int(input())

def action(func, num_list):
    r = 0
    for f in func:
                if f == 'R': # reverse 
                    r += 1 
                else:
                    if len(num_list) <= 0:
                        return 'error'
                    else:
                        if r%2 == 0:
                            num_list.popleft()
                        else:
                            num_list.pop()
    if r%2 == 0:
        return '['+','.join(num_list)+']'
    else:
        num_list.reverse()
        return '['+','.join(num_list)+']'
                

for _ in range(n):
    func = list(input().rstrip()) # 수행할 함수 입력 받음 
    num_length = int(input())
    num_list = deque(input().rstrip()[1:-1].split(','))
    if num_length == 0:
         num_list = []
    print(action(func, num_list))