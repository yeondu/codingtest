import sys 
import heapq
input = sys.stdin.readline 

n, k = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[k-1])

