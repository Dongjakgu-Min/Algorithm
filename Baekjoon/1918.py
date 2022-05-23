from sys import stdin
from collections import deque
import re

notation = deque(stdin.readline().strip())

postfix = []
stack = []
priority = {'*': 3, '/': }

while notation:
    alpha = notation.popleft()

    if re.match('[A-Z]', alpha):
        postfix.append(alpha)
    elif alpha == '(':
        stack.append(alpha)
    elif alpha == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    else:
        while stack and 
