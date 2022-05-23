import re
from collections import deque

def solution(expression):
    answer = 0
    result = [0]
    stack_n = []
    stack_s = []

    numbers = [int(i) for i in re.findall(r'\d+', expression)]
    sign = re.findall('[^0-9]', expression)
    calculator = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}

    def process(priority):
        while len(numbers) != 1:
            number = numbers.pop()
            stack_n.append(number)
            op = sign.pop()
            if op == priority[0]:
                stack_s.append(op)
            elif op == priority[1]:
                if len(stack_s) == 0:
                    stack_s.append(op)
                else:
                    stack_n.append(op)

        stack_n.append(numbers[0])

    process(['*', '+', '-'])
    print(stack_n)
    
    return answer

solution("100-200*300-500+20")