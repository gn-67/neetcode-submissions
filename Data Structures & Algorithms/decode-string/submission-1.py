class Solution:
    def decodeString(self, s: str) -> str:
        #i think we can use a single stack here
        #we can greedily iterate until we meet a closing bracket
        #once we meet a closing bracket, we pop until we meet our opening bracket, grabbing our value inside
        #then we pop until we reach a non-digit, which lets us grab our quantity
        #then we multiply the value by the quantity and append it back into the stack
        #this is so nested decoding can retrieve the previous value


        stack = []
        i = 0


        while i < len(s):
            if s[i] == "]": #we begin our popping sequence
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                #now we have aquired our string value, lets get the length
                stack.pop() #get rid of the opening bracket
                length = ""
                while stack and stack[-1].isdigit():
                    length = stack.pop() + length
        
                stack.append(string * int(length))
                i += 1
            
            else:
                stack.append(s[i])
                i += 1
        
        return "".join(stack)

        #2[a]3[b]. #2[a

        