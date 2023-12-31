def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) != 0 and stack[-1] == '(':  
                stack.pop()
            else:
                return False  
    
    return len(stack) == 0