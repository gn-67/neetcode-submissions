class Solution:
    def decodeString(self, s: str) -> str:
        #K is a valid input, input string is always well formed
        #go through sampel input after implementation

        #input is never empty
        #we can compute in one pass
        #we use a stack to maintain the length and character of our nested loops
        #and then whenever we 



        stack = []

        for i in range(len(s)):
            if s[i] == "]":
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring 
                stack.pop()
                length = ""
                while stack and stack[-1].isdigit():
                    length = stack.pop() + length
                stack.append(int(length) * substring)
            
            else:
                stack.append(s[i])
        
        return "".join(stack)


                    

        