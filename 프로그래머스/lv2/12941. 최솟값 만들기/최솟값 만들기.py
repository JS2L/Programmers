def solution(A, B):
    A.sort(reverse=True)  # A를 내림차순으로 정렬
    B.sort()  # B를 오름차순으로 정렬
    
    answer = sum(a * b for a, b in zip(A, B))
    return answer
