# create an empty stack
# when we come across an opening bracket, add it to the list
# when we come across a closing bracket, if the appropriate bracket is in at the top of the stack then pop it

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] =='{' or s[i] =='[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) != 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            elif s[i] == '}':
                if len(stack) != 0:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            elif s[i] == ']':
                if len(stack) != 0:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                        return False
        if len(stack) != 0:
            return False
        return True


        