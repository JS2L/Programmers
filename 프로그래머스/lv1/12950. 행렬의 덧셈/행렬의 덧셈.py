def solution(A,B):
    answer = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    return answer