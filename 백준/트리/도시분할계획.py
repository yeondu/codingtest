import sys 

input = sys.stdin.readline 

n, m = map(int, input().split()) # n: 집의 개수 m: 길의 개수 

graph = [list(map(int, input().split())) for _ in range(m)] # 길 생성 
graph = sorted(graph, key = lambda x: x[-1])
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x 


# 두 원소가 속한 집합 합치기 
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

weight = 0 

for i in graph: # 가중치가 작은 길부터 
    if find(i[0]) != find(i[1]): # 노드들의 루트 노드값이 다르다면 
        union(i[0], i[1]) # 루트 노드 변경 
        weight += i[-1] # 가중치 추가 
        last = i[-1]
        
print(weight - last) # 가장 마지막에 있는 가중치가 가장 크니까 해당 값을 빼줘야함