def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or a != answer[-1]:
            # 빈 배열에 answer[-1:]는 사용 가능 
            answer.append(a)
    return answer