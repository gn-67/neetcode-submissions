class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #since we need to keep track of a strictly increaing temperatures, we can use a monotonic stack

        result = [0] * len(temperatures)
        stack = []


        for i, temperature in enumerate(temperatures):

            while stack and stack[-1][0] < temperature:
                #if the current temp is greater than the 
                temp, tempInd = stack.pop()

                result[tempInd] = i - tempInd
            
            stack.append([temperature, i])
        
        return result 


        