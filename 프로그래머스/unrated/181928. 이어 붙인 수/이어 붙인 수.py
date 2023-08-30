def solution(num_list):
    hol_str = ""
    jjak_str = ""
    
    for num in num_list:
        if num % 2 == 0:
            jjak_str += str(num)
        else:
            hol_str += str(num)
    
    hol_sum = int(hol_str)
    jjak_sum = int(jjak_str)
    
    return hol_sum + jjak_sum
