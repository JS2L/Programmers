def solution(start_num, end_num):
    a = []
    for i in range(end_num+1) :
        a.append(i)   
    b = a[start_num:end_num+1]
    return b 