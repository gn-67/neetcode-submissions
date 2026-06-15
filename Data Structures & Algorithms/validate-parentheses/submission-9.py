class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close = {")" : "(", "]" : "[", "}" : "{"}


        for i in range(len(s)):
            if s[i] in close:
                if stack and stack[-1] == close[s[i]]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(s[i])
        
        if len(stack) != 0:
            return False
        return True

        