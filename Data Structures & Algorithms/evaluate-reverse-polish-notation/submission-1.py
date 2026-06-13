#add numbers to stack
#perform operations when we reach an operator
#pop the last two in stack, append new number
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = { "+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x,y: x / y}

        for i in range(len(tokens)):

            if tokens[i] not in ops:
                stack.append(tokens[i])

            elif tokens[i] in ops:
                total = ops[tokens[i]](int(stack[-2]), int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(total)


        return int(stack[0])

        