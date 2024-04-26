import sys 
import heapq
input = sys.stdin.readline 

n, k = map(int, input().split())

num_list = list(map(int, input().split()))
# heap = heapq.heapify(num_list) # 이렇게 별도로 저장하는게 아니라 heapq.heapify만 해도 됨
heapq.heapify(num_list)
print(num_list)
print(num_list[k-1])

