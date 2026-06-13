# solution is the DIFFERENCE between index of greater element and current element - how long it takes to get there
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures) 
        stack = [] #store the temp and the index as a pair

        for i, temp in enumerate(temperatures): #iterates thrgouh index and value of list

            while stack and temp > stack[-1][0]: #while the stack is NOT empty and the top is less than the current temp
                stackTemp, stackInd = stack.pop() #pop the top and store its values

                result[stackInd] = i - stackInd #the index of the popped value is now set to the current (greater) value minus the index of the popped value

            stack.append([temp, i]) #add to stack if the value is less than the top of the stack

        return result


        