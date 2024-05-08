from itertools import combinations 
import sys 
input = sys.stdin.readline 

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

combination = list(combinations(num_list, 3))
sum_comb = [sum(i) if sum(i)<=m else 0 for i in combination]

print(max(sum_comb))
