class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = [] 

        # we wanna use DFS to traverse our decisions, so lets make our helper functions

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy()) # we pass a copy bc we are still using and modifying cur aftert
                return

            if i >= len(nums) or total > target:
                return

            #we add current element to cur
            cur.append(nums[i])

            #first desicion
            dfs(i, cur, total + nums[i])
            #if this fails, we need to pop the failing element and continue with the next available element in nums
            cur.pop()
            dfs(i + 1, cur, total)
            

        #now we run dfs
        dfs(0, [], 0)
        return result
        