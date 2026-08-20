class Solution:
    def isValid(self, s: str) -> bool:
        # I think we can implement a stack data structure here to solve this problem
        #whenever we encounter a "closing" bracket, we should check the top of our stack to see if the appropriate openeing bracket preceeds, if it does then we continue, else we break and return false
        #additionally, if our stack has any elements left unprocessed, that means our input string doesn't contain its appropriate counterpart so we return false there too
        #otherwise if we clear all our checks, we return true


        #can a string potentially be empty?
        #can the string contain characters other than brackets



        #I can use a hashmap to keep track of the closing bracket + the opening we expect as key value pairs

        closing = { ")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for i in range(len(s)):
            if s[i] in closing:
                if stack and stack[-1] == closing[s[i]]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(s[i])
        

        if len(stack) > 0:
            return False
        
        return True
            

            


        