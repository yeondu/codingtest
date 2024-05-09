import sys 

input = sys.stdin.readline 

# 소수 여부 배열 생성
graph = [False]*2 + [True]*(2*123456-1)

primes = []

for i in range(2, 2*123456+1):
    if graph[i]:
        primes.append(i)
        graph[i] = False 
        for j in range(2*i, 2*123456+1, i):
            graph[j] = False


n = int(input())
while n != 0:
    count = len([i for i in primes if (i > n) and (i<=2*n)])
    print(count)
    n = int(input())