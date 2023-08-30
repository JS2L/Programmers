def solution(num):
    answer = 0
    
    while num != 1:
        if num % 2 == 0:
            num //= 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1
        
        if answer >= 500:  # 500번 이상 작업해도 1이 되지 않는 경우
            return -1
    
    return answer