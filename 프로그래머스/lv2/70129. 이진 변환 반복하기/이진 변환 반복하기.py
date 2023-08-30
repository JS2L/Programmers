
def solution(s):
    conversion_count = 0
    removed_zeros = 0
    
    while s != '1':
        removed_zeros += s.count('0')  # 0의 개수를 누적
        s = bin(s.count('1'))[2:]  # '1'의 개수를 2진법으로 변환한 문자열을 가져와서 저장
        conversion_count += 1
    
    return [conversion_count, removed_zeros]