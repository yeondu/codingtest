import sys 
input = sys.stdin.readline 

n = int(input())
budget = list(map(int, input().split()))
total = int(input()) # 총 예산 

if sum(budget) < total: # 총 예산보다 같거나 작다면 
    print(max(budget)) # 최대 예산값 출력 
else: # 최대 예산값 구하기 
    start = 0
    end = max(budget)

    while start <= end:
        total_num = 0
        mid = (start+end)//2
        for i in budget:
            if i < mid:
                total_num += i 
            else:
                total_num += mid 
        
        if total_num <= total:
            start = mid+1
        else:
            end = mid-1

    print(end)