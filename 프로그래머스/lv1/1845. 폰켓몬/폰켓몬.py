def solution(nums):
    max_c = len(nums)//2
    answer = []
    for i in nums :
        if i not in answer :
            answer.append(i)
    return len(answer) if max_c > len(answer) else max_c
     


# max 는 최대 가져갈수 있는 폰켓몬
# 새로운 배열을 만들어서 다른 숫자만 넣기
# 조건1 : 새 배열의 길이가 max보다 작으면 배열길이 return 아닐시 max return
# let answer = []; const max = nums.length / 2; nums.map(num => ( answer.length < max && !answer.includes(num) ? answer.push(num) : num )); return answer.length