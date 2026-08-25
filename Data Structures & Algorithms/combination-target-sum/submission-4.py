class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        #we can use a backtracking approach here 
        #we can traverse by building up a solution greedily
        #so we start with all of the first number, then once our solution goes over the target, we back track and start again
        #and we repeat this for each value 
        #and we can traverse by creating a dfs helper function



        result = []

        def dfs(i, cur, total):
            if total > target or i >= len(nums):
                return
            if total == target:
                result.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            dfs(i + 1, cur, total)
            return
        
        dfs(0, [], 0)
        return result

