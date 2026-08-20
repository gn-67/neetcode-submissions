class Solution:
    def decodeString(self, s: str) -> str:

	
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop() #get rid of the opening bracket
                length = ""
                while stack and stack[-1] in "0123456789":
                    length = stack.pop() + length
                stack.append(string * int(length))
                
            else:
                stack.append(s[i])
        return "".join(stack)


        