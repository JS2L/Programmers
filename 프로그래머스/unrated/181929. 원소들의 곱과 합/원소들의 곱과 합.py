def solution(list):
    double = sum(list)**2
    x = 1
    for i in list :
        x *= i
    if double < x :
        return 0
    elif double > x :
        return 1