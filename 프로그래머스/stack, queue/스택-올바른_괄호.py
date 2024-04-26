# test case만 통과 
def solution(s):
    answer = True
    
    data = list(s)
    answer_list = []
    
    for d in data:
        if len(answer_list)==0 and d == ')':
            return False
        elif len(answer_list)==0 or d == '(':
            answer_list.append(d)
            data.pop()
        elif answer_list[-1] == '(' and d == ')':
            data.pop()
            answer_list.pop(-1)
            
    if len(answer_list)>=2:
        return False
    else:
        return True
    
# 최종 제출에서 2개 실패
def solution(s):
    answer = True
    
    answer_list = []
    
    for d in s:
        if len(answer_list) == 0 and d == ')':
            return False
        elif len(answer_list) == 0:
            answer_list.append(d)
            answer = False
        elif answer_list[-1] != d:
            answer = True 
            answer_list.pop(-1)
        else:
            answer_list.append(d)
            answer = False
    return answer


# 최종 통과
def solution(s):
    
    answer_list = []
    
    for d in s:
        if d == '(':
            answer_list.append(d)
        else:
            if answer_list:
                answer_list.pop()
            else:
                return False
    if answer_list:
        return False
    
    return True
