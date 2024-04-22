# hash map 사용 
def solution(data):
    hash_map = {}
    
    for d in data:
        hash_map[d] = d
        
    for d in data:
        arr = ''
        
        for i in d:
            arr += i
            
            if arr in hash_map and arr != d:
                return False
    return True

# startswith 사용 
def solution(data):
    data.sort()
    
    for d1,d2 in zip(data, data[1:]):
        if d2.startswith(d1):
            return False
    return True



