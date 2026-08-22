class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #since we want to keep track of strictly increasing values, we need to make sure our stack contains only values that are decreeasing.
        #that way when we encounter a temperature that is greater, we can pop everything in the stack thats a smaller temp and update it in the result


        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, tempInd = stack.pop()
                result[tempInd] = i - tempInd
            
            stack.append([temperatures[i],i])
        
        return result