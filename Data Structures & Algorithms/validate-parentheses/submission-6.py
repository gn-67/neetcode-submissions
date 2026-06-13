class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for e in s:
            if e in closeToOpen:
                if stack and closeToOpen[e] == stack[-1]:
                    stack.pop()
                else:
                    return False #stack is empty or mismatch
                
            else:
                stack.append(e)
        if stack:
            return False
        return True
            
            