class Solution:
    def climbStairs(self, n: int) -> int:

        step1 = 1
        step2 = 1
        #topdown solution

        for step in range(n-1):
            temp = step1
            step1 = step1 + step2
            step2 = temp
        
        return step1



        