def solution(my_string, alp):
    # alp 문자열을 대문자로 변경
    upper_alp = alp.upper()
    
    # my_string 내에서 alp에 해당하는 문자들을 대문자로 변경하여 새 문자열 생성
    new_string = ''.join(upper_alp if c == alp else c for c in my_string)
    
    return new_string
