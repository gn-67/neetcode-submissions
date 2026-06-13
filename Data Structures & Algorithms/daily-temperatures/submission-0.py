# solution is the DIFFERENCE between index of greater element and current element - how long it takes to get there
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) 
        stack = [] #store the temp and the index as a pair

        for i, temp in enumerate(temperatures): #iterates thrgouh index and value of list
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()

                result[stackInd] = (i - stackInd)

            stack.append([temp, i])

        return result


        