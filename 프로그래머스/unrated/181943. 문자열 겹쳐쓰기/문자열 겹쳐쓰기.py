def solution(a, b, s):
    answer = ''
    if len(a[s:]) > (len(b)):
        answer = a[:s] + b + a[s+len(b):]
    else :
        answer = a[:s] + b        
    return answer