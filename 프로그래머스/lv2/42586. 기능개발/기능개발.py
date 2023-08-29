def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if progresses[0] + time*speeds[0] >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
                
            time += 1
    answer.append(count)
    return answer

# 프로그레스의 첫번째 + 횟수*시간이 100이 넘으면 처음꺼 지우고 카운트를 1 올려
# 그런데 다음것들도 그럴수 있으니 돌려지고 100이 넘으면 카운트를 1 더 올려
# 만약 100이 안넘는 else일때 time을 올려야 하는데 이걸 음...
# time을 늘려서 100이 넘도록 해줘야 해
# 그리고 카운트가 0초과 일때만 answer에 넣어줘야함