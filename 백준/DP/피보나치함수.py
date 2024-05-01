import sys 
input = sys.stdin.readline 

t = int(input())
hash = dict()

for i in range(0, 41):
    if i == 0:
        hash[i] = [1,0]
    elif i == 1:
        hash[i] = [0,1]
    else:
        hash[i] = [x+y for x, y in zip(hash[i-1], hash[i-2])]

for _ in range(t):
    n = int(input())
    print(' '.join(map(str,hash[n])))