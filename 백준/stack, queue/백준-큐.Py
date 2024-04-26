import sys 
input = sys.stdin.readline 

num = int(input())

queue = []

for _ in range(num):
    # text = list(input().strip().split(' '))
    text = input().split()
    if 'push' in text:
        queue.append(int(text[-1]))

    elif 'pop' in text:
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)

    elif 'size' in text:
        print(len(queue))

    elif 'front' in text:
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)

    elif 'empty' in text:
        if not queue:
            print(1)
        else:
            print(0)

    else:
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)