import sys 
input = sys.stdin.readline 

t = int(input())

for _ in range(t):
    n = int(input())
    days = [*map(int, input().split())]

    max_price = 0
    profit = 0

    # 미래의 가격부터 과거 시점까지 
    for i in range(n-1,-1,-1):
        if days[i] > max_price:
            max_price = days[i]
        else:
            profit += max_price - days[i]

    print(profit)