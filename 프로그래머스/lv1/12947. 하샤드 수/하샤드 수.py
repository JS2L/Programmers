def solution(x):
    a = list(map(int, str(x)))
    return True if x % sum(a) == 0 else False